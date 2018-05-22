import random
secret = random.randint(1,10)
print("第一个作品")

temp = input("输入你心中想的数字:")

guess = 0
num = 1
while guess != secret and num < 3:
    num += 1
    if temp.isdigit():
        try:
            guess = int(temp)
        except (ValueError,EOFError,KeyboardInterrupt):
            print('输入错误')
        temp = input("猜错了请重新输入:")
        guess = int(temp)
        if guess == secret:
            print("哥,对了对了")
            print("猜对了也没有奖励啊")
        else:
            if guess > secret:
                print("哥,大了大了")    
            else:
                print("嘿,小了!小了")
    else:
        temp = input("请重新输入:")
print("游戏结束啦")
