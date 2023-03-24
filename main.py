from src.dates.dates import dates
from src.prediction.prediction import prediction


def main():
    choice = input('Choice - "1" = prediction, "2" = dates: ')
    if choice == '1':
        prediction()
    elif choice == '2':
        dates()
    elif choice == 'e':
        pass
    else:
        print('For exit enter "e".', end=' ')
        main()


if __name__ == '__main__':
    main()
