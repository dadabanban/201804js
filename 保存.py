def save_file(file_name):

    name = open(file_name,'w')
    print('请输入文件内容，按:W退出:')
    while True:
        write = input()
        if write != ':W':
            name.write('s%\n' % write)
        else:
            break
    name.close()


file_name = input('请输入文件名:')
save_file(file_name)
