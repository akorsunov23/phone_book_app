from questions import questions


def main():
    while True:
        menu_book: str = input(
            "\nВыберите одно из пунктов меню (введите номер меню): \n"
            " 1. Прочитать весь справочник;\n"
            " 2. Добавить запись;\n"
            " 3. Редактировать запись;\n"
            " 4. Найти запись.\n\n"
            'Для выхода введите "exit": '
        )
        if menu_book == "exit":
            print("Вы завершили работу со справочником.")
            break
        elif menu_book not in ("1", "2", "3", "4"):
            print("\n!!! Введите номер соответствующего меню.")
        else:
            if menu_book == "1":
                questions.user_read_value()
            elif menu_book == "2":
                questions.user_add_value()
            elif menu_book == "3":
                questions.user_update_value()
            else:
                questions.user_search_value()


if __name__ == "__main__":
    main()
