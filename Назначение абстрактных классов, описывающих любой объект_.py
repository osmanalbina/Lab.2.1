import doctest
from abc import ABC, abstractmethod


class Appliance(ABC):
    def __init__(self, brand: str, power: int):
        """
        Создание и подготовкак работе объекта "Прибор"

        :param brand: Бренд прибора
        :param power: Мощность в ваттах

        Примеры:
        >>> appliance = Appliance("Samsung", 1500)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not isinstance(power, int) or power <= 0:
            raise ValueError("Мощность должна быть положительным целым числом")

        self.brand = brand
        self.power = power

    @abstractmethod
    def turn_on(self) -> None:
        """
        Включение прибора.
        """
        ...

    @abstractmethod
    def turn_off(self) -> None:
        """
        Выключение прибора.
        """
        ...


class Animal(ABC):
    def __init__(self, species: str, age: int):
        """
        Создание и подготовка к работе объекта "Животное"

        :param species: Вид животного
        :param age: Возраст животного

        Примеры:
        >>> animal = Animal("Собака", 5)  # инициализация экземпляра класса
        """
        if not isinstance(species, str):
            raise TypeError("Вид должен быть строкой")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом")

        self.species = species
        self.age = age

    @abstractmethod
    def make_sound(self) -> None:
        """
        Издание звука животным.
        """
        ...

    @abstractmethod
    def eat(self, food: str) -> None:
        """
        Кормление животного.

        :param food: Тип корма
        """
        ...


class Smartphone(ABC):
    def __init__(self, model: str, storage: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param model: Модель смартфона
        :param storage: Объем памяти в ГБ

        Примеры:
        >>> smartphone = Smartphone("iPhone", 128)  # инициализация экземпляра класса
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(storage, int) or storage <= 0:
            raise ValueError("Объем памяти должен быть положительным целым числом")

        self.model = model
        self.storage = storage

    @abstractmethod
    def make_call(self, number: str) -> None:
        """
        Совершение звонка.

        :param number: Номер телефона
        """
        ...

    @abstractmethod
    def install_app(self, app_name: str) -> None:
        """
        Установка приложения.

        :param app_name: Название приложения
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации