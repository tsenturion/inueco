def capitalize(text: str):
    if text == "":
        return ""

    if text is None:
        return None

    first_char = text[0].upper()
    rest_subsring = text[1:]
    return first_char + rest_subsring


