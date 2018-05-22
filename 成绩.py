password = 'passw'
count = 3
while count:
    passwo = input('请输入密码:')
    if passwo == password:
        print('密码正确')
        break
    elif '*' in passwo:
        print('密码不能有*,你还有', count, '次机会')
        continue
    else:
        print('密码错误,你还有', count-1, '次机会')
    count -= 1
