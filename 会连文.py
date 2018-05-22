def passs(yyf):
    lenth = len(yyf)
    last = lenth - 1
    lenth //= 2
    flag = 1
    for each in range(lenth):   
        if yyf[each] != yyf[last]:
            flag = 0
        
        last -= 1
    if flag == 1:
        return 1
    else:
        return 0
    
yyf = input("请输入你的对联:")
if passs(yyf) == 1:
    print("shi")
else:
    print("不是")
