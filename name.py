i = 1
flag = 0
x = 1
while i <= 10000:
    if (x % 2 == 1) and (x % 3 == 2) and (x % 5 == 4) and (x % 6 == 5) and (x % 7 == 0):
        flag = 1
    else:
        x = 7 * i
    i += 1
    
if flag == 1:
    print ("x的数值是",x)
else:
    print("没有答案")
