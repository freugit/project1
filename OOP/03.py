#继承的语法
#在Python中，任何类都有一个共同的父类叫object
class Person():
    name = "NoName"
    age = 0
    __score = 0 #考试成绩是秘密，只要自己知道
    _petname = "sec" #小名，是保护的，子类可以用，但不能公用，这个是约定俗成的不公用，实际可以访问。
    def sleep(self):
        print("Sleeping ......")
    def work(self):
        print("make some money")
#父类写在括号里
class Teacher(Person):
    teacher_id = 9517
    name = "dana" #子类变量名称与父类相同，优先使用子类的
    def make_test(self):
        print("attention")
    def work(self):
        #扩充父类的功能，只需要调用父类相应函数，
        super().work() #注意两种写法，还可以用Person().work(self)形式
        self.make_test()


t = Teacher()
print(t.name)
#print(t.__score) #私有变量不能访问，会报错，是通过改名实现的，因此会报变量名不存在
t.sleep()
print(t.teacher_id)
t.make_test()
t.work()

