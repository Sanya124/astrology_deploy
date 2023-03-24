from data.zodiacal_constellations import zodiacal_constellations

from src.general.color import error


def list_zodiacs() -> str:
    """List zodiacs in string with control characters.

    Returns:
        str: `1\t= aries\n...`
    """
    number_to_zodiac = __list_number_to_zodiac()
    list_zodiacs = '\n'.join(f'{num}\t= {value}' for num, value in number_to_zodiac.items())

    return list_zodiacs


def zodiac_and_dates(number: str) -> str:
    """Getting zodiac and it dates with control characters.

    Args:
        number: number month in list of zodiacs.

    Returns:
        str: `=> ZODIAC <= \nMonth day - Month day`
    """
    try:
        name = __list_number_to_zodiac().get(int(number))
        dates = ' - '.join(f'{k.capitalize()} {v}' for k, v in zodiacal_constellations[name].items())
        result = f"""=> {name.upper()} <= \n{dates}"""

        return result

    except ValueError:
        error('Enter only integer')


def __list_number_to_zodiac() -> dict:
    """List sequence number and zodiac.

    Returns:
        dict: `{1: 'zodiac', ...}`
    """
    return {number + 1: value for number, value in enumerate(zodiacal_constellations)}
