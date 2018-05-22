
def sum1(*pap,base = 3):
    sum2 = 0
    sum3 = 0
    for each in pap:
        sum2 += each
    
    sum2 *= base 
    return sum2
#print(sum3)
sum1(1,2,3,4,5,base = 5)
