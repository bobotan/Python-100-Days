class Tool(object):
    count=0
    def __init__(self,name):
        Tool.count+=1


t1=Tool('斧头')
t2=Tool('dao')
t3=Tool('cha')

t3.count=99
print(t3.count)
print(Tool.count)
print('==>%d'%t3.count)