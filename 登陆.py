

dict1 = {}

def new_user():
    ist = '请输入用户名:'
    while True:
        user = input(ist)
        if user in dict1:
            ist = ('此用户们已经被使用,请重新输入:')
            continue
        else:
            break
    pas = input('请输入密码:')
    dict1[user] = pas
    print('注册成功,赶紧试试登陆吧')

def old_user():
    ist = '请输入用户名'
    while True:
        user = input(ist)
        if user not in dict1:
            ist = '你输入的用户不存在,请重新输入'
            continue
        else:
            break
    pas = input ('请输入密码:')
    pwd = dict1.get(user)
    if pwd == pas:
        print('登陆成功')
    else:
        print('密码错误')

def showmenu():
    ist = '''
--新建用户:N--
--登陆账号:E--
--退出程序:Q--
请输入指令代码:'''
            

    while True:
        cho = input(ist)
        
        if cho not in 'NEQ':
            print('你的输入不正确')
        else:
            if cho == 'N':
                new_user()
            if cho == 'E':
                old_user()
            if cho == 'Q':
                break

showmenu()
    
'''

ist = int(input('请输入指令代码:'))

while 1:
    if ist == 'N':
        user = input('请输入用户名:')
        if user in dict1:
            user = ('此用户们已经被使用,请重新输入:')
        else:    
        
        pas = input('请输入密码:')
        dict1.fromkeys(user:pas)
    elif ist == 'E':
        '''
