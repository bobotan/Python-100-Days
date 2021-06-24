

def  read_binaryfile(filename):
    f= open(filename,'rb')
    i = 0
    while True:
        i += 1
        print(i)
        line = f.readline()
        if not line:
            break
        else:
            try:
                #             print(line)
                #             print(line.decode('utf8'))
                line.decode('utf8')
                # 为了暴露出错误，最好此处不print
            except:
                print(str(line))

read_binaryfile('C:\ProgramData\Homag Group\LicenseServer\License.dll')