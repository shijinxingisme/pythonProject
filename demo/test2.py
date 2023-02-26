# input
# a_input = input('please input sthing')
# print(a_input)

# 文件的读写
# text = 'text\nhello word!'
# print(text)
#
# my_file = open('file.txt', 'w')
# my_file.write(text)
# my_file.close()

# with open('file2.txt','w') as f2: #清空文件 然后写入
#     f2.write("nihao 6666 ")


# with open('file2.txt','a') as f2: #追加
#     f2.write("\n12121")
# with open('file2.txt', 'r') as f2:  #读
#     content = f2.read()
#     print(content)

# with open('file2.txt', 'r') as f2:  #读
#     # content = f2.readline()   #读取一行
#     content = f2.readlines()    #读取所有放列表中
#     print(content)

fileName = 'file2.txt'
with open(fileName) as f:
    for line in f:
        print(line)
