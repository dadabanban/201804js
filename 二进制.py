def ex(dec):
    res = [ ]
    res1 = " "
    while dec:
        t = dec % 2
        dec = dec // 2
        res.append(t)
    while res:
        res1 += str(res.pop())
    return res1

        
