"""

读取CSV文件

Version: 0.1
Author: 骆昊
Date: 2018-03-13python -m pip install --upgrade pip

"""

import csv

filename = 'Day01-15\Day11\example.csv'

try:
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print('无法打开文件:', filename)
else:
    for item in data:
        print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))
