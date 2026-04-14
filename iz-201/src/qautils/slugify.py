import re


def slugify(text: str) -> str:
    # нижний регистр
    text = text.lower()

    # пробелы и _ → -
    text = re.sub(r"[ _]+", "-", text)

    # удалить всё кроме a-z, 0-9 и -
    text = re.sub(r"[^a-z0-9-]", "", text)

    # схлопнуть дефисы
    text = re.sub(r"-+", "-", text)

    # обрезать дефисы по краям
    text = text.strip("-")

    return text