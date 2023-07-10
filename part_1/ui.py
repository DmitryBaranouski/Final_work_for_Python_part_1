import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите текст: '), number)
    body = check_len_text_input(
        input('Введите текст или описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nЭто программа 'Изменение'. Имеются следующие функции:\n\n1 - вывод всех заметок и текста из файла\n2 - добавление текста или заметок\n3 - удаление текста или заметок\n4 - редактирование текста или  заметок\n5 - выборка/выделение текста и/или заметок по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Мы будем Вас рады видеть снова у нас =). Всех благ! До новых встреч")