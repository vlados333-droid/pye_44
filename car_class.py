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


if '__main__' == __name__:
    # Примеры использования
    # Создание объектов
    car1 = Car("Toyota", "Camry", 2020, "чёрный")
    car2 = Car("Tesla", "Model S", 2023, "белый")

    # Вызов методов
    print(car1)  # Вывод информации о первом автомобиле
    car1.start_engine()  # Заводим двигатель
    car1.repaint("красный")  # Перекрашиваем автомобиль
    car1.stop_engine()  # Глушим двигатель

    print("\n")  # Разделитель для читаемости вывода

    print(car2)  # Вывод информации о втором автомобиле
    car2.start_engine()  # Заводим двигатель
    car2.stop_engine()  # Глушим двигатель
