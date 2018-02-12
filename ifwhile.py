import random
print('----------我爱你------------------------')
temp=input("不妨猜一下老婆现在心里想的是那个数字:")
guess=int(temp)
randomcount=random.randint(1,10)
print(randomcount)
while guess!=randomcount:
    if guess>randomcount:
        print("舞草,你猜大了,重新输入吧")
        temp=input()
        guess=int(temp)
    elif guess<randomcount:
        print("你猜小了,重新输入吧")
        temp=input()
        guess=int(temp)
print("猜中了,游戏结束")
