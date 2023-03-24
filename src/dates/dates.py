from src.dates.preparation_data import list_zodiacs, zodiac_and_dates


def dates() -> None:
    """Function for displays data by prediction."""
    print(list_zodiacs())
    zodiac = input('Enter number zodiac: ')
    print(zodiac_and_dates(zodiac))




