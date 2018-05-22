
def shui():
    for each in range(100,1000):
        a = each // 100
        b = each // 10 %10
        c = each % 10
        sum1 = a**3 + b**3 + c**3
        if sum1 == each:
            print(each)
        else:
            continue
