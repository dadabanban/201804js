def findstr(sub1,sub2):
    count = 0
    lenth = len(sub1)
    if sub2 in sub1:
        for each in range(lenth-1):
            if sub1[each] == sub2[0]:
                if sub1[each + 1] == sub2[1]:
                    count += 1
    print(count)
