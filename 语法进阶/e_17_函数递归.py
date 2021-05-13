def add_nums(num):
    if num == 1:
        return 1
    temp = add_nums(num - 1)
    return temp + num


result = add_nums(3)
print(result)
