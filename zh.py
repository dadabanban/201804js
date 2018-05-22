
def zh(x):
    res = ' '
    
    if x:
        res = zh(x//2)
        
        return res + str(x%2)
    else:
        return res
        

10
zh(10)
zh(5)
0
zh(5)
zh(1)
01
