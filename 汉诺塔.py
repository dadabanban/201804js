def hano(n,x,y,z):
    if n == 1:
        print(x,'->',y)
    else:
        hano(n-1,x,z,y)
        print(x,'->',z)
        hano(n-1,y,x,z)
n = int(input("请输入层数"))
hano(n,'x','y','z')
