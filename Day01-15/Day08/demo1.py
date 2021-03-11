

class Stu (object):
     def __init__(self,name,age):
         self.name=name
         self.age=age
     def sit(self):
         print(self.name)

if __name__=="__main__":
    stu=Stu(name='123',age=5)
    stu.sit()


