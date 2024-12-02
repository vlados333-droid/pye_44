class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sound = ''

    def make_sound(self):
        return self.sound


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sound = 'Meow'


if __name__ == '__main__':
    cat1 = Cat('Барсик', 3)

    print(cat1.make_sound())
