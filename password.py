symbol = r'''~!@#$%^&*()_=-/,.?<>;:[]{}\|'''
char = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'

passw = input('请输入密码：')

lens = len(passw)
while (passw.isspace() or len == 0) :
    passw = input("您输入的密码为空（或空格），请重新输入：")
if lens <= 8:
    ll = 0
elif  8 < lens <= 16:
    ll = 1
else:
    ll = 2

oo = 1

for each in passw:
    if each in symbol:
        oo += 1
        break
    
for each in passw:
    if each in char:
        oo += 1
        break
    
for each in passw:
    if each in num:
        oo += 1
        break
while 1:
    print ('您的:', end = ' ')
    if oo == 1 or ll == 0:
        print('低')

    elif oo == 2 or ll == 1:
        print('中')

    else:
        print('高')
    break

print("请按以下方式提升您的密码安全级别：\n\
\t1. 密码必须由数字、字母及特殊字符三种组合\n\
\t2. 密码只能由字母开头\n\
\t3. 密码长度不能低于16位'")

