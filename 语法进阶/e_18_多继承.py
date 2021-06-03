class A:
    def eat(self):
        print('eat')


class B:
    def sleep(self):
        print('sleep')


class C(A, B):
    pass


cc = C()
cc.sleep()
cc.eat()