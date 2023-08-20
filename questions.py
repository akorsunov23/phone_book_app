from config import QUESTION, CRITERIA
from phone_book import book


class QuestionsUser:
    """Опрос пользователя."""

    @staticmethod
    def _validate_data(key: int, value: str) -> bool:
        """Валидация входных данных."""

        if key == 1:
            if (len(value.split(" ")) == 3 and
                    value.replace(" ", "").isalpha()):
                return True
            return False
        elif key in (3, 4):
            if value.isdigit():
                return True
            return False
        else:
            return True

    @staticmethod
    def user_read_value():
        """Просмотр всех записей."""
        print("\n==Вы выбрали просмотр всего справочника:==\n")
        book.read_book()

    def user_add_value(self):
        """Опрос пользователя на пункт меню 'добавить запись'."""

        print("\n==Вы выбрали добавление новой записи==\n")
        values: list = []
        for key, val in QUESTION.items():
            while True:
                question: str = input(val)
                if self._validate_data(key=key, value=question):
                    values.append(question)
                    break
                print("Введите верные данные.")

        return book.add_val_book(values=values)

    def user_search_value(self):
        """Опрос пользователя по поиску записи в справочнике."""

        values: list = []
        print("\n==Вы выбрали поиск записи==\n")
        amount_criteria: int = int(
            input(f"{CRITERIA}По скольки критериям осуществлять поиск? ")
        )
        if 5 > amount_criteria > 1:
            while True:
                what_criteria: str = input(
                    f"{CRITERIA}Введите номера критерий через пробел: "
                )
                if (
                    len(what_criteria.split(" ")) > 1
                    and what_criteria.replace(" ", "").isdigit()
                ):
                    for key in what_criteria.split(" "):
                        while True:
                            question: str = input(QUESTION.get(int(key)))
                            if self._validate_data(
                                    key=key,
                                    value=question
                            ):
                                values.append(
                                    (
                                        int(key) - 1,
                                        question.title()
                                    )
                                )
                                break
                            print("Введите верные данные.")
                    return book.search_val_book(values=values)

        elif amount_criteria == 1:
            while True:
                what_criteria: str = input(f"{CRITERIA}Введите номера критерия: ")
                if what_criteria.isdigit() and int(what_criteria) < 5:
                    while True:
                        question: str = input(QUESTION.get(int(what_criteria)))
                        if self._validate_data(
                                key=int(what_criteria),
                                value=question
                        ):
                            values.append(
                                (
                                    int(what_criteria) - 1,
                                    question.title()
                                )
                            )
                            break
                        print("Введите верные данные.")
                return book.search_val_book(values=values)

        else:
            print(
                f"Ответ должен быть числом и не больше 4, Вы же ввели {amount_criteria}!"
            )
            return self.user_search_value()

    def user_update_value(self):
        """Опрос пользователя о редактировании записи."""

        print("\n==Вы выбрали редактирование записи==\n")
        max_num: int = book.read_book()
        numbers_contact: list = [num for num in range(1, max_num)]
        while True:
            try:
                contact: int = int(input("Введите номер контакта для редактирования: "))
                if contact in numbers_contact:
                    criteria: int = int(
                        input(f"{CRITERIA}Выберите критерию для редактирования: ")
                    )
                    if criteria > 4:
                        raise ValueError
                    while True:
                        new_value: str = input(QUESTION.get(criteria))
                        if self._validate_data(key=criteria, value=new_value):
                            values = {
                                "row": contact + 1,
                                "field": criteria,
                                "value": new_value,
                            }
                            return book.update_val_book(values=values)
                        print("Введите верные данные.")
                raise ValueError
            except ValueError:
                print("Введите число и не больше допустимого в списке!")


questions = QuestionsUser()
