# try:        #异常
#     file = open("haha",'r+')  #先去读读到 再写
# except Exception as e:
#     print(e)
fileName = "haha1"
try:        #异常

    file = open(fileName,'r+')  #先去读读到 再写
except Exception as e:
    print(e)
    res = input(' is create it ?')
    if (res =='yes'):
        with open(fileName,"w") as f:
            pass
        print("create haha ok")
    else:
        print('nothing')
        pass
else:   #没有错误
    file.write("nihaolihai")
    file.close()
