# str1='a1b2c3d4e5'
# print(str1[1])
# print(str1[2:5])
# print(str1[2:])
# print(str1.isdigit())
# print(str1.isalpha())
# print(str1.isalnum())
# print(str1[-3:-1])
# print(str1[::-1])





# 列表

# list1=[1,3,5,7,100]
# print(list1)
# list2=['fuck']*5
# print(list2)
# print(list2[2])
# list2.append('you')
# print(list2)


fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
for fruit in fruits:
    print(fruit.title(),end=' ')
print()

fruits3=fruits[:]
print(fruits3)