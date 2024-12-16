import doctest


class Cake:
    def __init__(self, name: str, price_per_kg: float, weight: float):
        """
        Создание и подготовка к работе объекта "Торт"

        :param name: Название торта
        :param price_per_kg: Цена за килограмм
        :param weight: Вес торта в кг

        Примеры:
        >>> cake = Cake("Медовик", 900, 2.5) # инициализация экземпляра класса
        """
        self.name = name
        if not isinstance(price_per_kg, (int, float)):
            raise TypeError("Цена за килограмм торта должна быть типа int или float")
        if price_per_kg <= 0:
            raise ValueError("Цена за килограмм торта должна быть положительным числом")
        self.price_per_kg = price_per_kg
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес торта должен быть типа int или float")
        if weight < 0:
            raise ValueError("Вес торта должен быть неотрицательным числом")
        self.weight = weight

    def calculate_the_cost(self) -> None:
        """
        Расчет стоимости торта.

        :return: Стоимость торта

        Примеры:
        >>> cake = Cake("Медовик", 900, 2.5)
        >>> cake.calculate_the_cost()
        """
        ...

    def calculate_the_discount(self, discount: int) -> None:
        """
        Расчет скидочной стоимости торта.
        :param discount: Скидка на торт

        :return: Стоимость торта

        Примеры:
        >>> cake = Cake("Медовик", 900, 2.5)
        >>> cake.calculate_the_discount(20)
        """
        if not isinstance(discount, int):
            raise TypeError("Скидка на торт должна быть типа int")
        if discount < 0:
            raise ValueError("Скидка на торт должна быть неотрицательным числом")
        ...

class Person:
    def __init__(self, name: str, age: int, gender: str):
        """
        Создание и подготовка к работе объекта "Человек"

        :param name: Имя человека
        :param age: Возраст человека
        :param gender: Пол человека

        Примеры:
        >>> person = Person("Виктория", 19, "женский")
        """
        self.name = name
        if not isinstance(age, int):
            raise TypeError("Возраст человека должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст человека должен быть положительным числом")
        self.age = age
        if gender not in ['мужской', 'женский']:
            raise ValueError("Пол человека должен быть 'мужской' или 'женский'")
        self.gender = gender

    def is_adult(self) -> bool:
        """
        Функция, которая проверяет, является ли человек совершеннолетним

        :return: Является ли человек совершеннолетним

        Примеры:
        >>> person = Person("Виктория", 19, "женский")
        >>> person.is_adult()
        """
        ...

    def get_info(self) -> str:
        """
        Получение информации о человеке

        :return: Информация о имени, возрасте и поле человека

        Примеры:
        >>> person = Person("Виктория", 19, "женский")
        >>> person.get_info()
        """
        ...

class BankAccount:
    def __init__(self, money: float):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param money: Количество денег на счету в рублях

        Примеры:
        >>> bank_account = BankAccount(5000) # инициализация экземпляра класса
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Количество денег на счету должно быть типа int или float")
        if money < 0:
            raise ValueError("Количество денег на счету должно быть неотрицательным числом")
        self.money = money

    def add_money_to_bank_account(self, add_money: float) -> None:
        """
        Добавление денег на счет.
        :param add_money: Добавляемые деньги в рублях

        Примеры:
        >>> bank_account = BankAccount(5000)
        >>> bank_account.add_money_to_bank_account(3200)
        """
        if not isinstance(add_money, (int, float)):
            raise TypeError("Добавляемые деньги должны быть типа int или float")
        if add_money < 0:
            raise ValueError("Добавляемые деньги должны быть неотрицательным числом")
        ...

    def withdrawal_money_from_bank_account(self, withdrawal_money: float) -> None:
        """
        Снятие денег со счета.

        :param withdrawal_money: Снимаемые деньги со счета в рублях
        :raise ValueError: Если количество снимаемых денег превышает количество денег на счете,
        то возвращается ошибка.

        :return: Объем реально снятых денег

        Примеры:
        >>> bank_account = BankAccount(5000)
        >>> bank_account.withdrawal_money_from_bank_account(3200)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
