def error(text: str) -> None:
    """Displaying data (error) with color accompaniment (red)."""
    print('\033[41mERROR:\033[0m', f'\033[31m{text}\033[0m', end=' ')


def positive(data: dict) -> None:
    """Displaying data with color accompaniment (green).

    Only for dicts to 'src/prediction/prediction.py' """
    list_zodiacs = ', '.join(f'\033[32m{el}\033[0m' for el in data['positive'])
    print('\033[42m\033[30mThis day is better for:\033[0m', list_zodiacs, sep='\t', end='\n' * 2)


def neutral(data: dict) -> None:
    """Displaying data with color accompaniment (yellow).

    Only for dicts to 'src/prediction/prediction.py' """
    list_zodiacs = ', '.join(f'\033[33m{el}\033[0m' for el in data['neutral'])
    print('\033[43m\033[30mThis day neutral for:\033[0m', list_zodiacs, sep='\t', end='\n' * 2)


def negative(data: dict) -> None:
    """Displaying data with color accompaniment (red).

    Only for dicts to 'src/prediction/prediction.py' """
    list_zodiacs = ', '.join(f'\033[31m{el}\033[0m' for el in data['negative'])
    print('\033[41m\033[30mWe do not recommend:\033[0m', list_zodiacs, sep='\t', end='\n' * 2)
