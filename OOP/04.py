#构造函数的概念
class Animal():
    pass
class PaxingAni(Animal):
    def __init__(self):
        print("PaXing DongWu")

class Dog(PaxingAni):
    #__init__就是构造函数
    #每次实例化的时候，第一个被自动的调用
    #因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("I am init a dog")
class Cat(PaxingAni):
    pass
#实例化的时候，自动调用了Dog的构造函数
#因为找到了构造函数，则不再查找父类的构造函数
kaka = Dog()
#因为Cat没有构造函数，则往上查找构造函数，因为在PaxingAni找到了构造函数，则不再向上查找
c = Cat()

