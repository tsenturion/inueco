def parse_port(value):
    """Преобразует value в номер порта (int) и валидирует диапазон."""

    # bool — отдельная ветка (хотя это subclass int)
    if isinstance(value, bool):
        raise TypeError("bool is not a valid port type")

    # int
    if isinstance(value, int):
        if 1 <= value <= 65535:
            return value
        raise ValueError("port out of range")

    # str
    if isinstance(value, str):
        value = value.strip()

        if not value:
            raise ValueError("empty string")

        if not value.isdigit():
            raise ValueError("invalid string")

        port = int(value)

        if 1 <= port <= 65535:
            return port
        raise ValueError("port out of range")

    # другие типы
    raise TypeError("unsupported type")