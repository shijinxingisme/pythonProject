import random as r

n= r.randint(1,100)
atep =0
print('game start')


def getNum():
    guessn = input(' input num 1-100')
    while True:
        if guessn.isdigit():
            return int(guessn)
        else:
            guessn = input(' input num 1-100')

# guess = int(input(' input num 1-100'))
guess = getNum()
low=1
high=100
while True:
    atep+=1
    print('step',atep)
    if guess == 0: #退出
        print('quit game')
        break
    if guess<n:
        print("数字小了")
        low=guess+1
    elif guess>n:
        print("数字大了")
        high=guess-1
    else:
        print("猜对了一共猜了"+str(atep)+"步")
        break
    print("你可以试试这个区间的",low,"-",high)
    guess=getNum()
    # guess = int(input(' input num 1-100'))
print('game over')
