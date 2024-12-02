class Car:
    """Класс, представляющий автомобиль."""

    def __init__(self, brand, model, year, color):
        """
        Конструктор для инициализации автомобиля.

        :param brand: Марка автомобиля (например, "Toyota").
        :param model: Модель автомобиля (например, "Camry").
        :param year: Год выпуска.
        :param color: Цвет автомобиля.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False  # Флаг, указывает, заведён ли автомобиль

    def start_engine(self):
        """Запускает двигатель."""
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} теперь заведён.")
        else:
            print(f"{self.brand} {self.model} уже работает.")

    def stop_engine(self):
        """Останавливает двигатель."""
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} теперь выключен.")
        else:
            print(f"{self.brand} {self.model} уже выключен.")

    def repaint(self, new_color):
        """
        Перекрашивает автомобиль в новый цвет.

        :param new_color: Новый цвет.
        """
        print(f"{self.brand} {self.model} перекрашен из {self.color} в {new_color}.")
        self.color = new_color

    def __str__(self):
        """Возвращает строковое представление автомобиля."""
        return f"{self.year} {self.brand} {self.model}, цвет: {self.color}"


class Truck(Car):
    """
    Класс, представляющий грузовик, наследуется от класса Car.
    """

    def __init__(self, brand, model, year, color):
        """
        Конструктор для инициализации грузовика.

        :param brand: Марка грузовика.
        :param model: Модель грузовика.
        :param year: Год выпуска.
        :param color: Цвет грузовика.
        """
        super().__init__(brand, model, year, color)
        self.is_loaded = False  # Атрибут, указывает, загружен ли грузовик

    def load(self):
        """
        Загружает грузовик.
        """
        if not self.is_loaded:
            self.is_loaded = True
            print(f"{self.brand} {self.model} теперь загружен.")
        else:
            print(f"{self.brand} {self.model} уже загружен.")

    def unload(self):
        """
        Выгружает грузовик.
        """
        if self.is_loaded:
            self.is_loaded = False
            print(f"{self.brand} {self.model} теперь выгружен.")
        else:
            print(f"{self.brand} {self.model} уже пуст.")

    def __str__(self):
        """
        Возвращает строковое представление грузовика.
        """
        load_status = "загружен" if self.is_loaded else "пуст"
        return f"{super().__str__()}, состояние: {load_status}"


if '__main__' == __name__:
    # Создание объекта класса Truck
    truck1 = Truck("Volvo", "FH16", 2021, "синий")

    # Вызов методов для грузовика
    print(truck1)  # Вывод информации о грузовике
    truck1.start_engine()  # Заводим двигатель
    truck1.load()  # Загружаем грузовик
    print(truck1)  # Вывод информации после загрузки
    truck1.unload()  # Выгружаем грузовик
    truck1.stop_engine()  # Глушим двигатель
