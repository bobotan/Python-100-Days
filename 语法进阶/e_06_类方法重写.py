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

    def eat(self):
        # 使用super().方法
        # super().eat()
        # 使用 父类.方法
        # Dog.eat(self)
        print('哮天犬eat')


xtq = XiaoTianQuan()
xtq.eat()
