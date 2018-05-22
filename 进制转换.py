
inf = input("请输入一个整数(输入Q结束程序):")
while inf != 'q':
    inf1 = int(inf)
    print("十进制 -> 十六进制:%d -> %x" %(inf1,inf1))
    inf = input("请输入一个整数(输入Q结束程序):")
    if inf == 'q':
        break
    else:
        continue
