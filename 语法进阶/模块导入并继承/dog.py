from animal import Animal


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


xiaohuang = Dog('小黄')
xiaohuang.eat()
