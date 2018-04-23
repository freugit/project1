'''
定义一个学生类，用来形容学生
'''
#定义一个空的类
class Student():
    #一个空类，pass代表直接跳过
    #此处pass必须有
    pass
mingyue = Student()

#再定义一个类，用来描述听Python的学生
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = "Python0"
    #需要注意
    #1.def dohomework的缩进层级
    #2.系统默认有一个self参数
    def dohomework(self):
        print("I 在做作业")

        #推荐在函数末尾使用return语句
        return None
#实例化一个叫yueyue的学生，是一个具体的人
#实例化时，对象并没有立即建立自己的成员变量，所有成员变量与类成员变量是同一个
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传递进入参数
yueyue.dohomework()

# 赋值实例的成员变量后，实例的成员变量与类的成员对象就不再是同一个了
yueyue.name = "yueyue"
yueyue.age = 17

print(yueyue.name)
print(yueyue.age)

#但本身类的成员变量没有改变
print(PythonStudent.name)
print(PythonStudent.age)


#关于self的案例
class A():
    name = "liuYing"
    age =18
    def __init__(self):
        self.name = "aaaaa"
        self.age = 200
    def say(self):
        print(self.name)
        print(self.age)
class B():
    name = "bbbbb"
    age = 90
a = A()
#此时，系统会默认把a作为第一个参数传入函数
a.say()
#使用类名调用方法时，不会自动传入参数，因此要手动传入参数，此时，self被a替换
A.say(a)
#只要有参数，参数有name和age属性，都照单全收，以下代码都可以运行
A.say(A)
A.say(B)
#以上代码，利用了鸭子模型