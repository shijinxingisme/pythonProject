
# ---- while
# num = 1
#
# while num<5:
#     print(num)
#     num+=1
# ----

# for i in range(6):
#     print(i)

# for i in range(4,6):
#     print(i)

# for i in range(4,16,4):
#     print(i)

# list
# a_list = [1,2,3,55,99,55,66,77,88]
# print(a_list)
# print(a_list[6])
# print(a_list[-6])
# print(a_list[3:5])
# print(a_list[:5])
# print(a_list[5:])
# print(a_list[:])
#
# for i in a_list:
#     print(i)
# print(len(a_list))
# print(a_list.index(3))
# print(a_list.count(55),a_list.count(8))
# a_list.sort()
# a_list.sort(reverse=True)  #倒叙
# print(a_list)

#列表的操作
# a_list = [1,2,3,55,99,55,66,77,88]
# a_list[1]=100      #修改
# a_list.append(12)  #追加
# a_list.insert(2,20)  #在某个位置插入
# del a_list[2]   #删除某个位置
# a_list.remove(55)      #删除数组的某个值
# a=a_list.pop()      #移除尾部到某个值
# print(a_list)
# print(a)

# 多维数组
# b_list = [[1,2,3],[4,5,6],[7,8,9]]
# print(b_list[1])
# print(b_list[2][1])
# numpy

# 元组
# a_tuple=(1,2,4,66,223)
# b_tuple=6,24,42,616,2323
# print(a_tuple[1:4])
# print(b_tuple)
# for i in a_tuple:
#     print(i)
# 不能排序   不能加值 值是固定的
# '''
# > 大于
# '''
# #if
# a =1
# b=2
# c=3
# d=1
# if a==d:
#     print("666")
# if a<b<c:
#     print("right")
# if a<b>c:
#     print("right")
# if a ==b:
#     print("true")
# elif a==c:
#     print("false")
# elif a==d:
#     # print("a==d")
#     pass            #不执行任何操作
# else:
#     print("null")


'''
and
or
'''
# a=1
# b=2
# c=3
# d=1

# if a<b and a==d:
#     print("right")
# if a>b or a==d:
#     print("right")

colors = ["red","blue","blank","green"]
# for color in colors:
#     if color== 'blank':
#         print("blank11")
#     else:
#         print("no have blank")
#
# if 'red' in colors:
#     print("red")

# if colors:      #有值返回true
#     print("have vel")
# else:
#     print("null")

#字典
# a_list=[1,2,3,4]
# d = {'pen':7,'apple':3,'applepen':10}
# d['a']=11
# print(d)
# del d['pen']
# print(d)
# for k,v in d.items():   #遍历整个字段的键值对
#     print(v)
# for a in d.keys():   #key
#     print(a)
# for a in d.values():   #values
#     print(a)
# for key in sorted(d.values()):  #排序字典
#     print(key)

'''
函数
'''
# a = 100
# def function(): #定义一个函数
#     global a        #使用全局变量
#     b=2
#     c=a+b
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
#     print("a+b=",c)
#
# #调用
# function()
#
# def function1(a,b):
#     print(a+b)
#
# function1(1,2)
#
# def addRes(a,b):
#     return a+b
#
# print(addRes(1,2))

'''
模块
'''

def func_max(a,b):
    return a+b
