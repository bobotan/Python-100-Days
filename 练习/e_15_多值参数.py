def demo(num,*args,**kwargs):
    print(num)
    print(args)
    print(kwargs)

def sum_numbser(*args):
    num=0
    for n in args:
        num+=n
    return  num
def sum_args(args):
    num=0
    for n in args:
        num+=n
    return  num



result=sum_numbser(1,2,3,4,5)
print(result)

result2=sum_args((1,2,3,4,5))
print(result2)