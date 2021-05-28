class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('[%s]eat something' % self.name)
