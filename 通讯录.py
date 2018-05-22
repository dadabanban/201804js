print('''
1.查询通讯录
2.增加联系人
3.删除联系人
4.推出程序

''')
con = dict()

while 1:
    strr = int(input('请输入指令:'))
    
    if strr == 1:
        name = input("请输入姓名:")
        if name in con:
            
            print (name + ':' +con[name])
        else:
            print('输入的不在名单内')
    if strr == 2:
        
        name = input('请输入姓名')
        if name in con:
            print('你输入的姓名已经存在')
            print(name + ':' + con[name])
            if input('是否修改电话') == 'yes':
                
                 con[name] = input('请输入电话')
        else:
            con[name] = input('请输入电话')

    if strr == 3:
        name = input('请输入姓名')
        if name in con:
            del(con[name])
        else:
            print('姓名不存在')

    if strr == 4:
        break
print('欢迎使用本程序')
