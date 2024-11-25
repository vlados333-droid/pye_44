def read_file():
    file_name = input('Введите имя файла: ')

    try:
        with open(file_name, 'r') as file:
            print("Содержимое файла: ")
            print(file.read())

    except FileNotFoundError:
        print(f'Файл {file_name} не найден')

    except PermissionError:
        print(f'Недостаточно прав для открытия файла {file_name}')

    except Exception as e:
        print(f'Произошла непредвиденная ошибка: {e}')


def safe_input():
    while True:
        try:
            number = int(input("Введите число: "))
            print(f'Вы ввели число: {number}')
            break

        except ValueError:
            print('Это не целое число! Введите целое число!')


if __name__ == '__main__':
    safe_input()

    read_file()
