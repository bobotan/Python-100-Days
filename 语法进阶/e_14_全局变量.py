num = 10


def demo1():
    global num
    num = 99
    print('demo1===>%d' % num)


def demo2():
    num = 88
    print('demo2===>%d' % num)


demo1()
demo2()
print('num===>%d' % num)
