from src.general.color import negative, neutral, positive
from src.general.functions import char_to_month
from src.prediction.zodiac import favorability_and_zodiac


def prediction() -> None:
    """Function for displays data by prediction."""
    month = input(f'Enter month: {char_to_month()}: ')
    day = input('Enter the date of the month: ')
    data = favorability_and_zodiac(day=day, month=month)
    for item in [positive, neutral, negative]:
        item(data)
