class Transport:
    """
    Базовый класс Транспортные средства.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства (ТС).

        :param brand: Марка ТС.
        :param model: Модель ТС.
        :param year: Год выпуска ТС.
        """
        self._brand = brand
        self._model = model
        self._year = year

    @property
    def brand(self) -> str:
        """Возвращает марку ТС."""
        return self._brand

    @property
    def model(self) -> str:
        """Возвращает модель ТС."""
        return self._model

    @property
    def year(self) -> int:
        """Возвращает год выпуска ТС."""
        return self._year

    def get_info(self) -> str:
        """
        Получить информацию о ТС.

        :return: Строка с ТС.
        """
        return f"{self._year} {self._brand} {self._model}"

    def __str__(self) -> str:
        return f"Марка: {self.brand}. Модель: {self.model}. Год выпуска: {self.year}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year})"


class Car(Transport):
    """
    Дочерний класс для легковых автомобилей, наследует от Transport.
    """

    def __init__(self, brand: str, model: str, year: int, passenger_seats: int) -> None:
        """
        Инициализация легкового автомобиля.

        :param brand: Марка легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param passenger_seats: Количество мест для пассажиров в автомобиле.

        Перегрузка метода добавляет атрибут
        `passenger_seats`, который специфичен для легковых автомобилей и
        не представлен в базовом классе.
        """
        super().__init__(brand, model, year)
        self._passenger_seats = passenger_seats

    @property
    def passenger_seats(self) -> int:
        """Возвращает количество мест для пассажиров в легковом автомобиле."""
        return self._passenger_seats

    def get_info(self) -> str:
        """
        Получить информацию о легковом автомобиле.

        :return: Строка с информацией о легковом автомобиле.
        """
        return f"{super().get_info()}, {self.passenger_seats}" # Перегруженный метод, чтобы добавить информацию о количестве пассажирских мест

    def __str__(self) -> str:
        return f"{super.__str__()}. Количество пассажирских мест: {self.passenger_seats}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year}, passenger_seats={self.passenger_seats})"

class Truck(Transport):
    """
    Дочерний класс для грузовых автомобилей, наследует от Transport.
    """

    def __init__(self, brand: str, model: str, year: int, capacity: float) -> None:
        """
        Инициализация грузового автомобиля.

        :param brand: Марка грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param capacity: Грузоподъемность грузового автомобиля (т).

        Перегрузка метода добавляет атрибут
        `capacity`, который специфичен для грузовых автомобилей и
        не представлен в базовом классе.

        """
        super().__init__(brand, model, year)
        self._capacity = capacity

    @property
    def capacity(self) -> float:
        """Возвращает грузоподъемность грузового автомобиля (т)."""
        return self._capacity

    def get_info(self) -> str:
        """
        Получить информацию о грузовом автомобиле, включая грузоподъемность.

        :return: Строка с информацией о грузовом автомобиле.
        """
        return f"{super().get_info()}, {self.capacity}"  # Перегруженный метод, чтобы добавить информацию о грузоподъемности

    def __str__(self) -> str:
        return f"{super.__str__()}. Грузоподъемность: {self._capacity}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year}, capacity={self.capacity})"

if __name__ == "__main__":
    # Write your solution here
    pass
