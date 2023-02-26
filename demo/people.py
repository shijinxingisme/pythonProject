class people:   #类
    def __init__(self,name='zs',age=10):
        self.name=name
        self.age=age
        print("init =======")
    def getName(self):
        print("name is :",self.name+" 11")
    def getAge(self):
        print("age is :", self.age)
    def eat(self):
        print("eat")
    def think(self,a,b):
        print("a+b:"+a+b)
# p  = people()
# # print(p.name)
# print(p.getName())

class student(people):
    def __init__(self,grade =1,school='MIT'):
        super().__init__()  #父类的初始化
        self.grade=grade
        self.school=school
        self.scroe=100
        print('student init')
    def learn(self):
        print('learning')
    def my_school(self):
        print('my school is ',self.school)
    def eat(self):
        print("eat222")
    # pass
stu1 = student()
stu1.getName()
stu1.learn()
stu1.my_school()
stu1.eat()
