import requests

from bs4 import BeautifulSoup
from typing import Dict

from data.mappings import mapping_zodiac, mapping_favorability_to_class


def parse(response: requests.Response) -> Dict[str, dict]:
    """Parsing response from Website 'https://deployhoroscope.ru/'.

    Args:
        response: requests.Response by URL = 'https://deployhoroscope.ru/'.

    Returns:
        Dict[str, dict]: `{'favorability': {'zodiac': [1, 2, ...], ...}, ...}`
    """
    result = {'positive': {}, 'neutral': {}, 'negative': {}}
    soup = BeautifulSoup(response.text, 'lxml')
    rows = soup.tbody.find_all('tr')
    for row in rows:
        zodiac_ = row.find('td', class_='text-uppercase').text
        zodiac = ''.join(char for char in zodiac_ if char.isalnum())
        for days, class_ in mapping_favorability_to_class.items():
            result[days][mapping_zodiac[zodiac]] = [int(value) for value in row.find('td', class_=class_).text.split()]

    return result
