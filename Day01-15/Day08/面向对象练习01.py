class student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def study(self,course_name):
        print('%s 正在学习 %s'%(self.name,course_name))
    def watch_av(self):
        if(self.age<18):
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情动作片.' % self.name)



class Test:
    def __init__(self,foo):
        self.__fuck=foo
    def __bar(self):
        print(self.__fuck)
        print('__bar')

def main():
    people=student('bobotan',32)
    people.study('python程序设计')
    people.watch_av()

    test=Test('cuvk')
    test._Test__bar()


if  __name__ == '__main__':
    main()

