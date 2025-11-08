import sys
import argparse
import asyncio
import contextlib
from typing import Awaitable, Callable

import httpx
import aiohttp
import ssl
import random

# ----------  фрагменты, оформленные как функции ----------

REQUEST_TIMEOUT = httpx.Timeout(connect=2.0, read=5.0, write=5.0, pool=2.0)
POOL = httpx.Limits(max_connections=200, max_keepalive_connections=50)
MAX_BYTES = 5 * 1024 * 1024  # 5 MiB
PING_INTERVAL = 10.0

async def demo_httpx_get(url: str) -> None:
    async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
        r = await client.get(url)
        r.raise_for_status()
        print(r.json())

async def demo_httpx_h2(url: str) -> None:
    async with httpx.AsyncClient(limits=POOL, http2=True) as client:
        r = await client.get(url)
        r.raise_for_status()
        print(r.http_version, len(r.content))

async def demo_httpx_deadline(url: str) -> None:
    async with httpx.AsyncClient() as client:
        async with asyncio.timeout(6.0):
            r = await client.get(url, timeout=httpx.Timeout(connect=2.0, read=5.0))
        r.raise_for_status()
        print(len(r.content))

async def demo_httpx_retry(url: str, attempts: int = 3) -> None:
    base = 0.2
    async with httpx.AsyncClient() as client:
        for i in range(1, attempts + 1):
            try:
                r = await client.get(url)
                r.raise_for_status()
                print(r.status_code)
                return
            except (httpx.ConnectError, httpx.ReadTimeout, httpx.RemoteProtocolError):
                if i == attempts:
                    raise
                delay = min(base * (2 ** (i - 1)) + random.uniform(0.0, base), 5.0)
                await asyncio.sleep(delay)

async def demo_batch_get(urls: list[str], concurrency: int = 50) -> None:
    sem = asyncio.Semaphore(concurrency)
    async with httpx.AsyncClient() as client:
        async def one(u: str) -> tuple[str, int]:
            async with sem:
                r = await client.get(u)
                r.raise_for_status()
                return u, r.status_code

        tasks = [asyncio.create_task(one(u)) for u in urls]
        async for fut in _as_completed_iter(tasks):
            try:
                u, code = await fut
                print(u, code)
            except Exception as e:
                print("error", repr(e), file=sys.stderr)

async def _as_completed_iter(tasks):
    for fut in asyncio.as_completed(tasks):
        yield fut

async def demo_stream_to_file(url: str, path: str, chunk: int = 64 * 1024) -> None:
    async with httpx.AsyncClient() as c:
        async with c.stream("GET", url) as r:
            r.raise_for_status()
            with open(path, "wb") as f:
                async for part in r.aiter_bytes(chunk_size=chunk):
                    f.write(part)
    print(f"saved to {path}")

async def demo_get_capped(url: str) -> None:
    async with httpx.AsyncClient() as c:
        async with c.stream("GET", url) as r:
            r.raise_for_status()
            size = 0
            async for chunk in r.aiter_bytes():
                size += len(chunk)
                if size > MAX_BYTES:
                    raise ValueError("response too large")
    print("ok, size <=", MAX_BYTES)

async def demo_proxy_tls(url: str, proxy: str | None) -> None:
    ctx = ssl.create_default_context()
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    async with httpx.AsyncClient(verify=ctx, proxies=proxy) as client:
        r = await client.get(url)
        r.raise_for_status()
        print(r.http_version)

async def demo_ws_client(url: str) -> None:
    async with aiohttp.ClientSession(trust_env=True) as s:
        async with s.ws_connect(url, heartbeat=PING_INTERVAL) as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    print(msg.data)
                elif msg.type in (aiohttp.WSMsgType.CLOSE, aiohttp.WSMsgType.ERROR):
                    break

async def demo_ws_reconnect(url: str, base: float = 0.5, max_delay: float = 30.0) -> None:
    attempt = 0
    async with aiohttp.ClientSession(trust_env=True) as s:
        while True:
            ws = None
            try:
                ws = await s.ws_connect(url, heartbeat=10.0)
                attempt = 0
                while True:
                    msg = await ws.receive()
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        print(msg.data)
                    elif msg.type in (aiohttp.WSMsgType.CLOSED, aiohttp.WSMsgType.ERROR):
                        raise ConnectionError
            except (aiohttp.ClientError, ConnectionError, asyncio.TimeoutError):
                attempt += 1
                delay = min(base * (2 ** (attempt - 1)), max_delay)
                await asyncio.sleep(delay)
            finally:
                if ws is not None:
                    with contextlib.suppress(Exception):
                        await ws.close()

async def demo_structured(urls: list[str], ws_url: str, deadline: float = 30.0) -> None:
    async def http_batch():
        async with httpx.AsyncClient() as c:
            await asyncio.gather(*(c.get(u) for u in urls))

    async def ws_forever():
        async with aiohttp.ClientSession(trust_env=True) as s:
            async with s.ws_connect(ws_url, heartbeat=10.0) as ws:
                async for msg in ws:
                    _ = msg.data  # consume

    async with asyncio.timeout(deadline):
        async with asyncio.TaskGroup() as tg:
            tg.create_task(http_batch())
            tg.create_task(ws_forever())

# ---------- CLI (единая точка входа) ----------

Command = Callable[[argparse.Namespace], Awaitable[int]]

def _run(coro: Awaitable[None]) -> int:
    # единый запуск event loop + код возврата
    try:
        asyncio.run(coro)
        return 0
    except KeyboardInterrupt:
        print("Interrupted", file=sys.stderr)
        return 130
    except Exception as e:
        print(f"Error: {e!r}", file=sys.stderr)
        return 1

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="net-demos", description="Async HTTP/WebSocket demos")
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("httpx-get", help="GET c фазовыми таймаутами")
    g.add_argument("--url", required=True)

    h2 = sub.add_parser("httpx-h2", help="GET с HTTP/2 и лимитами пула")
    h2.add_argument("--url", required=True)

    dl = sub.add_parser("deadline", help="GET под общим дедлайном")
    dl.add_argument("--url", required=True)

    rt = sub.add_parser("retry", help="GET с retry и джиттером")
    rt.add_argument("--url", required=True)
    rt.add_argument("--attempts", type=int, default=3)

    bg = sub.add_parser("batch", help="Параллельный батч с семафором")
    bg.add_argument("--urls", nargs="+", required=True)
    bg.add_argument("--concurrency", type=int, default=50)

    st = sub.add_parser("stream", help="Потоковая загрузка в файл")
    st.add_argument("--url", required=True)
    st.add_argument("--path", required=True)

    cp = sub.add_parser("capped", help="Загрузка с ограничением размера")
    cp.add_argument("--url", required=True)

    px = sub.add_parser("proxy-tls", help="Прокси + кастомный TLS контекст")
    px.add_argument("--url", required=True)
    px.add_argument("--proxy", default=None)

    ws = sub.add_parser("ws", help="Базовый WebSocket клиент")
    ws.add_argument("--url", required=True)

    wsr = sub.add_parser("ws-reconnect", help="WebSocket с переподключением")
    wsr.add_argument("--url", required=True)

    sg = sub.add_parser("structured", help="HTTP-батч + WebSocket под дедлайном")
    sg.add_argument("--urls", nargs="+", required=True)
    sg.add_argument("--ws-url", required=True)
    sg.add_argument("--deadline", type=float, default=30.0)

    return p

def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.cmd == "httpx-get":
        return _run(demo_httpx_get(args.url))
    if args.cmd == "httpx-h2":
        return _run(demo_httpx_h2(args.url))
    if args.cmd == "deadline":
        return _run(demo_httpx_deadline(args.url))
    if args.cmd == "retry":
        return _run(demo_httpx_retry(args.url, args.attempts))
    if args.cmd == "batch":
        return _run(demo_batch_get(args.urls, args.concurrency))
    if args.cmd == "stream":
        return _run(demo_stream_to_file(args.url, args.path))
    if args.cmd == "capped":
        return _run(demo_get_capped(args.url))
    if args.cmd == "proxy-tls":
        return _run(demo_proxy_tls(args.url, args.proxy))
    if args.cmd == "ws":
        return _run(demo_ws_client(args.url))
    if args.cmd == "ws-reconnect":
        return _run(demo_ws_reconnect(args.url))
    if args.cmd == "structured":
        return _run(demo_structured(args.urls, args.ws_url, args.deadline))

    print("Unknown command", file=sys.stderr)
    return 2

if __name__ == "__main__":
    sys.exit(main())

# команда для запуска
# python .\main.py httpx-get --url https://api.github.com/rate_limit