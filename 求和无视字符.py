sum1 = int(input("请输入一个列表;"))
sum2 = 0

for each in sum1: 
    if type(each) == type(2):    
        sum2 = each + sum2
    else:
        continue



print(sum2)
'''


def sum(x):
    result = 0
    
    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else:
            continue

    return result

print(sum([1, 2.1, 2.3, 'a', '1', True]))
'''
