def print_line(char, times):
    """
    打印单行分隔符
    :param char:
    :param times:
    :return:
    """
    print(char * times)


def printlines(char, times):
    '''
    打印多行分隔符
    :param char:
    :param times:
    :return:
    '''
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1
