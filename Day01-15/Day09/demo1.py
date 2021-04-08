class Persion():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @staticmethod
    def is_valid(age):
        return age.isdigit()

    # method
    def play(self):
        if self._age <= 16:
            print('%s 玩泥巴。' % self._name)
        else:
            print('%s 看电影' % self._name)


if __name__ == '__main__':
    if (Persion.is_valid('12')):
        persion = Persion('wangdachu', 17)
        persion.name = 'bobotan'
        persion.age = 12
        persion.play()
