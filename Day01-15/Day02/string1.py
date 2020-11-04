"""
进制转换
"""
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))  # 在前面加“#”，则带进制前缀

"""
左中右对齐及位数补全
（1）< （默认）左对齐、> 右对齐、^ 中间对齐、= （只用于数字）在小数点后进行补齐

（2）取位数“{:4s}”、"{:.2f}"等
"""
print('{} and {}'.format('hello','world'))  # 默认左对齐
print('{:10s} and {:>10s}'.format('hello','world'))  # 取10位左对齐，取10位右对齐
print('{:^10s} and {:^10s}'.format('hello','world'))  # 取10位中间对齐
print('{} is {:.2f}'.format(1.123,1.123))  # 取2位小数
print('{0} is {0:>10.2f}'.format(1.123))  # 取2位小数，右对齐，取10位
print('{:<30}'.format('left aligned'))  # 左对齐
print('{:>30}'.format('right aligned'))  # 右对齐
print('{:^30}'.format('centered'))  # 中间对齐
print('{:*^30}'.format('centered'))  # 使用“*”填充
print('{:0=30}'.format(11))  # 还有“=”只能应用于数字，这种方法可用“>”代替

"""
百分数%
"""

points=19
total=22
print('Correct answers: {:.2%}'.format(points/total))


name='      fuck\t\ngongyuheng    '
print(name)
print(name.lstrip())
print(name.rstrip())

