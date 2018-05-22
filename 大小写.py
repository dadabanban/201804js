

counta = 0 #前面的大写字母
countb = 0 #小写字母
countc = 0 #后面的大写字母

if str1[i].isupper():

    if countb:
        countc += 1
    else:
        counta += 1
        countc = 0

if str1[i].isslower():

    if counta != 3:
        counta = 0
        countb = 0
        countc = 0
    else:
        if countb:
            counta = 0
            countb = 0
            countc = 0
        else:
            countb = 1
            countc = 0
            taget = i
if counta == 3 and countc == 3:
    print(str1[i],end = ' ')
    counta = 3
    countb = 0
    countc = 0
    
            
        

