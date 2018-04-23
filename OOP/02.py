# 私有变量实例
class Person():
    #name是公有的成员
    name = "Liuying"
    #__age就是私有成员
    __age = 18
p = Person()
#打印公有成员
print(p.name)
#打印私有成员，出错
#print(p.__age)
#不是真私有，可以通过以下方式访问
print(p._Person__age)
