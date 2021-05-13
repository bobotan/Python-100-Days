class Animal():
    def eat(self):
        print('eat')

    def drink(self):
        print('drink')

    def run(self):
        print('run')


class Dog(Animal):
    """"""

    def bark(self):
        print('往往就')


class XiaoTianQuan(Dog):
    def fly(self):
        print('飞')


xtq = XiaoTianQuan()
xtq.eat()
