import requests
import sys

from src.general.color import error
from src.general.functions import char_to_month
from src.prediction.parsing_rows_with_html import parse


def favorability_and_zodiac(day: str, month: str, url: str = 'https://deployhoroscope.ru/') -> dict:
    """Function of getting data by URL and structuring.

    Args:
        day:    number of day - 1, ... 31;
        month:  number of month - "C", "N";
        url:    address to application with data.

    Returns:
        dict:   `{'positive': [], 'neutral': [], 'negative': []}`
    """
    try:
        if month.upper() == 'C':
            url = url
        elif month.upper() == 'N':
            url += 'next-month'
        else:
            raise KeyError

        response = requests.get(url)
        day = int(day)
        result = __dict_of_favorability_and_zodiac(data=parse(response), day=day)

        return result

    except requests.ConnectionError:
        error('Сheck your internet connection')

    except KeyError:
        error(f'You must select month: {char_to_month()}.')
        sys.exit()

    except ValueError:
        error('Invalid value. You must enter day as integer: [1, .. 31]')
        sys.exit()


def __dict_of_favorability_and_zodiac(data: dict, day: int) -> dict:
    """Parsing response in structure.

    Args:
        data:   data of parsing html, `{'favorability': {'zodiac': [1,2,3],...}, ...}`;
        day:    day of month.

    Returns:
        dict:   `{'favorability': ['zodiac', ...], ...}`
    """
    result = {}
    for item in ['positive', 'neutral', 'negative']:
        result[item] = [key for key, value in data[item].items() if day in value]

    return result
