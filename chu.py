res = [ ]
def chu(x):
   
    if x > 0:
        res.insert(0,x%10)

        chu(x//10)

    else:
        print(res)
