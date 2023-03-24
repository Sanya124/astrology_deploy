from data.mappings import mapping_char_to_month


def char_to_month():
    """Displayed symbol and description."""
    return ", ".join(f'"{char}" - {desc}' for char, desc in mapping_char_to_month.items())
