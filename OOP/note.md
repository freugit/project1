# 写在前面的话
- 跟出版社合作
    - 【阅轩图书专营店-天猫】（http://detail.tmall.com/item.htm?id=535882394166）
    - 推荐图书-【Python编程从入门到实践】（https://login.tmall.com/?from=sm&redirect）
- 邮箱
    - 我们会教给大家用python发送邮件
    - 对邮箱进行设置，只要设置好了，通过邮箱地址和授权码就能发送邮件
    - 愿意的话可以联系 1320365896（qq）
- 下周一课程临时改录制
- 下周三开始，前端课程并行讲课

# 0. OOP-Python面向对象
- Python的面向对象
- 面向对象编程
    - 基础
    - 公有私有
    - 继承
    - 组合，Mixin
- 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数
# 1. 面向对象编程（ObjectOriented,OO）
- OOP思想
    - 接触到任意一个任务，首先想到的是任务这个世界的构成，是由模型构成的
- 几个名词
    - OO：面向对象
    - OOA：面向对象的分析
    - OOD：面向对象的设计
    - OOI：XXX的实现
    - OOP：XXX的编程
    - OOA->OOD->OOI：面向对象的实现过程
- 类和对象的概念
    - 类：抽象名词，代表一个集合，共性的事物  
    - 对象：具象的事物，单个个体
    - 类跟对象的关系    
        - 一个是具象，代表一类事物的某一个个体
        - 一个是抽象，代表的是一大类事物
- 类中的内容，应该具有两个内容
    - 表明事物的特征，叫做属性（变量）
    - 表明事物功能或动作，成为成员方法（函数）
# 2.类的基本实现
- 类的命名
    - 遵守变量命名的规则
    - 大驼峰（由一个或者多个单词构成，每个单词首字母大写，单词跟单词直接相连）
    - 尽量避开跟系统命名相似的命名
- 如何声明一个类
    - 必须用class关键字
    - 类由属性和方法构成，其它不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值，使用None
    - 案例 01.py
- 实例化类
    - 变量 = 类名（） #实例化了一个对象
- 访问对象成员
    - 使用点操作符
        - obj.成员属性名称
        - obj.成员方法
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有成员检查
        - dict前后各有两个下划线
        - obj.__dict__
    - 
# 3. anaconda基本使用
- anaconda主要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda list:显示anaconda安装的包
- conda env list：显示anaconda的虚拟环境列表
- conda create -n xxx python=3.6 创建python版本为3.6的虚拟环境，名称为xxx
# 4.类与对象的成员分析
- 类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
- 类存储成员时使用的是与类关联的一个对象，名称是类名的一个实例
- 独享存储成员时存储在当前对象中
- 对象访问一个成员时，如果对象中没有该成员，尝试访问类中的同名成员
    - 在不对对象的成员变量进行赋值的情况下，对象的成员变量与类的成员变量是同一个
    - 如果对象中有此成员，一定使用对象中的成员
- 创建对象的时候，类中的成员不会自动放入对象当中，而是得到一个空对象，没有成员
- 通过对象对类中成员重新赋值或通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员
# 5.关于self
- self在对象的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数（无论名字叫self还是其他）
- self并不是关键字，而是一个用于接受对象的普通参数，理论上可以用任何一个普通变量名代替
- 方法中有self形参的方法称为非绑定类的方法，可以通过对象访问，没有self（即是没有任何参数）的是绑定类的方法，只能通过类访问，使用类访问绑定类的方法是使用类实例名
- 如果类方法中需要访问当前类的成员，可以使用__class__.变量名来访问
- 类实例使用类方法时不会自动传入第一个参数
# 6.面向对象的三大特性
- 封装
- 继承
- 多态
## 6.1 封装
- 封装就是对对象的成员进行访问限制，
- 封装的三个级别：
    - 公开：public
    - 受保护的：protected
    - 私有的：private
    - public，private，protected不是关键字
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
- 私有
    - 私有成员时最高级别的封装，只能在当前类或对象中访问
    - 在成员前面添加两个下划线即可
        class Person():
            # name 是共有的成员
            name = "Liuying"
            # __age就是私有成员
            __age = 18
    - 案例见02.py
    - Python的私有不是真私有，是一种称为name mangling的改名策略，检测到__变量名会更改成别的名字，可以通过对象.类名__变量名访问
- 受保护的封装 protected
    - 受保护的封装是将对象成员进行一定级别的封装，然后在类中或者子类中都可以进行访问，但是在外部都不可以
    - 封装方法，在成员名称前添加一个下划线即可
- 公开的，公共的，public
    - 公开的封装实际对成员没有任何操作，任何地方都可以访问
## 6.2 继承
- 继承是一个类可以获得另外一个类中的成员属性和成员方法
- 作用：减少代码，增加代码的复用功能，同时可以设置类与类直接的关系
- 继承与被继承的概念
    - 被继承的类叫父类，也叫基类，也叫超类
    - 用于继承的类叫子类，也叫派生类
    - 继承与被继承的关系一定存在一个is-a关系
- 继承的语法，案例见03.py
- 继承的特征
    - 所有类都继承自object类，即所有的类都是object类的子类
    - 子类一旦继承父类，则可以使用父类中除私有成员外的所有内容
    - 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
    - 子类中可以定义独有的成员属性和方法
    - 子类中定义的成员和父类成员如果相同，则优先使用子类成员
    - 子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码重用。可以使用父类名.父类成员的格式来调用父类成员，也可以使用super().父类成员的格式来调用
    - 案例见03.py    
- 继承变量函数的查找顺序问题
    - 优先查找自己的变量
    - 没有则查找父类
    - 构造函数如果本类没有定义，则自动查找调用父类的构造函数
    - 如果本类有定义，则不在继续向上查找
- 构造函数
    - 是一类特殊的函数，在类进行实例化之前进行调用，案例见04.py
    - 如果定义了构造函数，则实例化使用自己的构造函数，不查找父类构造函数
    - 如果没有定义，则自动查找父类的构造函数
    - 如果子类没有定义，父类的构造函数带参数，则构造函数的参数应该按父类参数构造
- super
    - super不是关键字，而是一个类
    - super的作用是获取MRO(MethodResolustionOrder)列表中的第一个类
    - super与父类直接没有任何实质性的关系，但通过super可以调用到父类
    - super使用两个方法，参见在构造函数中调用父类的构造函数
- 单继承和多继承
    - 单继承：每个类只能继承一个类
    - 多继承：每个类允许继承多个类
- 单继承和多继承的优缺点
    - 单继承：
        - 优点：传承有序逻辑清晰语法简单隐患少
        - 缺点：功能不能无限扩展，只能在当前唯一的继承链中扩展
    - 多继承：
        - 优点：类的功能扩展方便
        - 缺点：继承关系混乱
    - 菱形继承/钻石继承问题：
        - 多个子类继承自同一个父类，这些子类被同一个类继承，于是继承关系图形成一个菱形图谱
        - MRO
        - 关于多继承的MRO
            - MRO就是多继承中，用于保存继承顺序的一个列表
            - Python本身采用C3算法来对多继承的菱形继承进行计算的结果
            - MRO列表的计算原则：
                - 子类永远在父类前面、
                - 如果多个父类，则根据继承语法中括号内类中的书写顺序存放
                - 如果多个类继承了同一个父类，孙子类只会选取继承语法括号中第一个父类的父类
## 6.3 多态
- 多态就是同一个对象在不同情况下有不同的状态出现
- 多态不是语法，是一种设计思想
- 多态性：一种调用方式，不同的执行效果
- 多态：同一事物的多种形态，动物分为人、猪、狗等
- 多态和多态性

- Mixin设计模式
    - 主要采用多继承方式对类的功能进行扩展
    。。。。。
- 我们使用多继承语法来实现Minxin
- 使用Mixin实现多继承的时候要非常小心、
    - 首先他必须表示某一单一功能，而不是某个物品
    - 职责必须单一，如果有多个功能，则写多个Mixin
    - Mixin不能依赖于子类的实现
    - 子类即使没有继承这个Mixin类，也能照样工作，只是缺少了某个功能
- 优点：
    - 使用Mixin可以在不对类进行任何修改的情况下，扩充功能
    - 可以方便的组织和维护不同功能组件的划分
    - 可以根据需要任意调整功能类的组合
    - 可以避免创建很多新的类，导致类的继承混乱     
# 7. 类的相关函数
    - issubclass:检查一个类是否是另一个类的子类
    - isinstance:检查一个对象是否是一个类的实例
    - hasattr:检测一个对象是否有成员xxxx
    - getattr:
    - setattr:
    - delattr:
    - dir：获取对象的成员列表
# 8.类与对象的三种方法
- 实例方法
    - 需要实例化对象才能使用的方法，使用过程中可能需要截止对象的其他对象方法完成
- 静态方法
    - 不需要实例化，通过类直接访问
- 类方法
    - 不需要实例化
- 三个方法具体区别自行百度
# 9.抽象类
    - 抽象方法：没有具体实现内容的方法为抽象方法
    - 抽象方法的主要意义是规范了子类的行为和接口
    - 抽象类的使用需要借助abc模块
    import abc
    - 抽象类：包含抽象方法的类叫抽象类，通常称为abc类
    - 抽象类的使用
        - 抽象类可以包含抽象方法，也可以包含具体方法
        - 抽象类中可以有方法也可以有属性
        - 抽象类不允许直接实例化
        - 必须继承才可以使用，且继承的子类必须实现所有继承的抽象方法
        - 假定子类没有实现所有的抽象方法，则子类也不能实例化
        - 抽象类的主要作用是设定类的标准，以便于开发的时候具有统一的规范
        
# 10.自定义类
    - 类其实是一个类定义和各种方法的自由组合
    - 可以定义
    
# 模块
- 一个模块就是一个包含python代码的文件，后缀名是.py就可以，模块就是个python文件
- 为什么我们用模块
    - 程序太大，编写维护非常不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，所以任何代码可以直接书写
    - 不过根据模块的规范，最好在模块中编写以下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
- 如何使用模块
    - 模块直接导入
    - 语法
        import module_name
        module_name.function_name
        module_name.class_name
    - 模块文件不能以数字开头，因为被引用时，变成以数字开头的变量，不合法。
      示例，06.py不能以模块形式被引用，而p01.py可以以模块形式被引用
      万一是数字开头命名文件，可以用importlib包间接使用
      例子：
      import importlib
      tuling = importlib.import_module("06") #把原来06模块重命名为tuling    
    - import 模块 as 别名
        - 导入的同时给模块起一个别名
        - 其余用法跟第一种相同
    - from module_name import func_name,class_name
        - 按上述方法有选择性的导入
        - 使用的时候可以直接使用导入的内容，不需要前缀
    - from module_name import *
        - 好处在于不需要前缀使用
        - 弊端在于防止不了命名重复
- if __name__ == "__main__"的使用
    - 可以有效避免模块代码被导入的时候被动执行的问题
    - 建议所有程序的入口都以此代码作为入口 

# 2. 模块的搜索路径和存储
- 什么是模块的搜索路径
    - 加载模块的时候，系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径
        import sys
        sys.path 属性可以获取这些路径
- 添加搜索路径
    - sys.path.append(dir)
- 模块的加载顺序
    1. 上搜索内存中已加载好的模块
    2. 搜索python的内置模块
    3. 搜索sys.path的路径
# 包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一块的文件夹就是包
- 自定义包的结构
    |---包
    |---|---__init__.py 包的标志文件
    |---|--- 模块 1
    |---|--- 模块 2
    |---|---|---__init__.py 包的标志文件
    |---|---|--- 子包模块 1
    |---|---|--- 子包模块 2
- 包的导入操作
    - import package_name
        - 直接导入一个包，可以使用__init__.py的内容
        - 使用方式是：
                package_name.func_name()
                package_name.class_name.func_name()
        - 此种方式访问的内容是
        - 案例 08.py
    - import package_name as p
        - 具体用法跟作用方式，跟上述简单导入一致
        - 注意的是此种方式是默认对__init__的内容的导入
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
                package.module.func_name
                package.module.class.func()
                package.module.class.var
        - 案例 09.py
    - import package.module as pm
- from ... import 导入
    - from package import module
    - 此种导入方法不执行__init__的内容
            from pk01 import p01
            p01.sayHello
    - from package import *
        - 导入当前包 __init__.py 文件中所有的函数和类
        - 使用方法
                func_name()
                class_name.func_name
                class_name.var
- from package_module import *
    - 导入包中指定的模块的所有内容
    - 使用方法
            func_name()
            class_name.func_name()
- 在开发环境中经常会使用其它模块，可以在当前包中直接导入其它模块的内容
    - import 完整的包或模块的路径
- "__all__"的用法
    - 在使用from package import * 的时候，* 可以导入的内容
    - "__init__.py"中如果文件为空，或者没有"__all__"，那么只可以把__init__中的内容导入
    - "__init__.py"如果设置了"__all__"的值，那么则按照"__all__"指定的子包或者模块进行导入，如此则不会导入"__init__"中的内容
    - "__all__ =["module1","module2","package1"...]"    
    - 案例10.py 
    - 使用时需要用 module1.func()
# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
- 作用是防止命名冲突
        setName()
        Student.setName()
        Dog.setName
# 调试技术
- 调试流程：单元测试—>集成测试->交测试部
- 分类：
    - 静态调试：
    - 动态调试：
# pdb调试
- pdb：python 调试库
# pycharm调试
- run/debug模式 案例 11.py
- 断点，程序的某一行，程序在debug模式下，遇到断点就会暂停
# 单元测试


# LOG
- https://www.cnblogs.com/yyds/p/6901864.html
- logging
- logging模块提供模块级别的函数记录日志
- 包括四大组件
## 1.日志相关概念
- 日志
- 日志级别（level）
    - 不同的用户关注不同的程序信息,下面级别由低到高:
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO操作=>不要频繁操作
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - log4j
    - log4php
    - logging
# 2.logging模块
- 日志级别
    - 级别可自定义
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- 初始化/写日志实例需要指定级别，只有当级别等于或高于指定级别才被记录
- 使用方式
    - 直接使用logging(封装了其它组件)
    - logging四大组件直接定制
#2.1 logging模块级别的日志
- 使用以下几个函数
    - logging.debug(msg,*args,**kwargs)创建一条严重级别为DEBUG的日志记录
    - logging.info创建一条严重级别为INFO的日志记录
    - logging.warning创建一条严重级别为WARNING的日志记录
    - logging.error创建一条严重级别为ERROR的日志记录
    - logging.critical创建一条严重级别为CRITICAL的日志记录
    - logging.log(level,*args,**kwargs)创建一条严重级别为level的日志记录
    - logging.basicConfig(**kwargs)对root logger进行一次性配置
- logging.baseConfig(**kwargs)对root logger进行一次性配置
    - 只在第一次调用的时候起作用
    - 不配置logger则使用默认值：
        - 输出：sys.stderr
        - 级别：WARNING
        - 格式：level:log_name:content
- 案例 12.py
- format 参数
    - %(name)s Logger的名字
    - %(levelno)s 数字形式的日志级别
    - %(levelname)s 文本形式的日志级别
    - %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
    - %(filename)s 调用日志输出函数的模块的文件名
    - %(module)s 调用日志输出函数的模块名
    - %(funcName)s 调用日志输出函数的函数名
    - %(lineno)d 调用日志输出函数的语句所在的代码行
    - %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
    - %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
    - %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
    - %(thread)d 线程ID。可能没有
    - %(threadName)s 线程名。可能没有
    - %(process)d 进程ID。可能没有
    - %(message)s用户输出的消息
# 2.2 logging模块的处理流程
- 四大组件
    - 日志器（Logger）：产生日志的一个接口
    - 处理器（Handler）:把产生的日志发送到相应的目的地
    - 过滤器（Filter）：更精细的控制那些日志输出
    - 格式器（Formatter）:对输出信息进行格式化
- logger
    - 产生一个日志
    - 操作
        - logger.setLevel()设置日志器将会处理的日志消息的最低严重级别
        - logger.addHandler()和logger.removeHandler 为改logger对象添加或者移除一个Handler
        - logger.addFilter()和logger.removeFilter 为改logger对象添加或者移除一个Filter
        - logger.debug:产生一条debug级别的日志，同理，info，error等
        - logger.exception():创建类似于logger.error的日志消息
        - logger.log()：获取一个明确的日志level参数创建一个日志记录
    - 如何得到一个logger对象
        - 实例化
        - logging.getLogger()
- Handler
    - 把log发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter,removeFilter
    - 不需要直接使用，Handler是基类
        logging.StreamHandler
        logging.FileHandler
        logging.handlers.RotatingFileHandler
        logging.handlers.TimeRotaingFileHandler
        logging.handlers.HTTPHandler
        logging.handlers.SMTPHandler
        logging.NullHandler
- Format类
    - 直接实例化
    - 可以继承Format添加特殊内容
    - 三个参数
        - fmt:指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
        - datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d-%H-%M-%S"
        - style：python 3.2新增的参数，可取值为"%","{"和"""
    - 案例13.py


# 环境
- xubuntu
- anaconda
- pycharm
- python3.6
- https://www.cnblogs.com/jokerbj/p/7460260.html
- http://www.dabeaz.com/python/UnderstandingGIL.pdf
# 多线程 vs 多进程
- 程序：一堆代码以文本形式存入一个文档
- 进程：程序运行的一个状态
    - 包含地址空间，内存，数据栈等
    - 每个进程有自己完全独立的运行环境，多进程共享数据是一个问题
- 线程
    - 一个进程的独立运行片段，一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程间共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释锁（GIL）
    - python代码的执行是python虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行
- Python包
    - thread：有问题，不好用，python3改成了_thread
    - threading:通行的包
- 案例14.py 老的_thread包的应用
- threading的使用
    - 直接利用threading.Thread生成Thread实例
        1. t = threading.Thread(target = xxx,args = (xxx,))
        2. t.start():启动多线程
        3. t.join():等待多线程执行完成
        4. 案例15.py
        - 守护线程daemon
            - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束时自动退出
            - 一般认为，守护线程不重要或者不允许离开主线程独立运行
            - 守护线程案例能否有效跟环境相关 案例16.py
        - 线程的常用属性
            - threading.currentThread:返回当前线程变量
            - threading.enumerate返回一个包含正在运行线程的list，正在运行是在开始后结束前
            - threading.activeCount:返回正在运行的线程数量
            - thr.setName:给线程起个名字
            - thr.getName:得到线程的名字
        - 直接继承threading.Thread
            - 直接继承Thread
            - 重写run函数
            - 类案例可以直接运行
        - 另一种写法见案例17
- 共享变量
    - 共享变量：当多个线程同时访问一个变量时，会产生共享变量的问题
    - 案例18.py 
    - 解决变量：锁，信号灯。
    - 锁（LOCK）：
        - 是一个标准：表示一个线程在占用一些资源
        - 使用方法
            - 上锁
            - 使用共享资源，放心的用
            - 取消锁，释放锁
        - 案例19.py
        - 锁谁：哪个资源需要多个线程共享，锁哪个
        - 理解锁：锁其实不是锁住谁，而是一个令牌
    - 线程安全问题：
        - 如果一个资源/变量，它对于多个线程来讲，不用加锁也不会引起任何问题，则称为线程安全
        - 线程不安全变量类型：list,set,dict
        - 线程安全变量类型：queue
    - 生产者消费者问题
        - 一个模型，可以用来搭建消息队列，案例20.py
        - queue是一个用来存放变量的数据结构，特点是先进先出，内部元素排队，可以理解成一个特殊的list
    - 死锁问题，案例21.py
    - 死锁解决方法，案例22.py
    - semaphore 信号灯:
        - 允许一个资源最多由几个多线程同时使用，案例23.py
    - Timer 案例24.py
        - Timer是利用多线程，在指定时间后启动一个线程
    - 可重入锁
        - 一个锁，可以被一个线程多次申请
        - 主要解决递归调用的时候，需要申请锁的情况
        - 案例 25.py
        
# 线程替代方案
- subprocess
    - 完全跳过线程，使用进程
    - 是python线程的主要替代方案
    - python2.4后引入
- multiprocess
    - 使用threading接口派生，使用子进程
    - 允许为多核或者cpu派生进程，接口与threading非常相似
    - python2.6

- concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
    - python3.2后引入
# 多进程
- 进程间通讯（InterprocessCommunication,IPC）
- 进程之间无任何共享状态
- 进程的创建
    - 直接生成Process实例对象，案例26
    - 派生子类，案例27
- 在os中查看pid,ppid以及他们之间的关系
    - 案例28
    
- 生产者消费者模型
    - JoinableQueue 
    - 案例29   
    - 队列中哨兵的使用，案例30
   

# 结构化文件存储
- xml json
- 为了解决不同设备之间的信息交换
- xml
- json
- xml文件
- 参考资料
    - https://docs.python.org/3/library/xml.etree.elementtree.html
    - http://www.runoob.com/python/python-xml.html
    - https://blog.csdn.net/seetheworld518/article/details/49535285
- xml(eXtensibleMarkupLanguage) 可扩展标记语言
    - 标记语言，语言中使用尖括号括起来的文本字符串标记
    - 可扩展：用户可以自己定义需要的标记
    - 例如：
            <Teacher>
                自定义标记Teacher
                在两个标记之间任何内容都应该跟Teacher相关
            </Teacher>
    - 是w3c组织制定的一个标准
    - xml描述的是数据本身：即数据的结构和语义
    - HTML侧重于如何显示web页面中的数据
    
- xml文件的构成
    - 处理指令（可以认为一个文件内只有一个处理指令）
        - 最多只有一行
        - 且必须在第一行
        - 内容是与xml本身处理相关的一些声明和指令
        - 以xml关键字开头
            - 一般用于声明xml的版本和采用的编码
                - version属性时必须的
                - encoding属性用来指出xml解释器使用的编码
            - 根元素有且只能有一个
        - 子元素
        - 属性
        - 内容
            - 表明标签所存储的信息
        - 注释
            - 起说明作用的信息
            - 注释不能嵌套在标签内
            - 只有在注释的开始和结尾使用双短横线
            - 三短横线只能出现在注释的开头而不能用在结尾
        
    - 保留字符的使用
        - xml中使用的符号可能跟实际符号相冲突，典型就是左右尖括号
        - 使用实体引用(EntityReference)来表示保留字符
                <score>score>80</score> 有错误，xml不能出现>
                <score>score&gt;80</score>使用实体引用
        - 把含有保留字符的部分放在CDATA块内部，CDATA块把内部信息视为不需要转义
                <![CDATA[
                    select name,age
                    from Student
                    where score>80
                    ]]>   
        - 常用的需要转义的保留字符和对应实体引用
            - &:&amp；
            - <:&lt；           
            - >:&gt；
            - ':&apos；
            - ":&quot；
            - 一共五个，每个实体引用都以&开头并且以分号结尾
    - xml标签的命名规则
        - Pascal命名法
        - 以单词表示，第一个字母大写
        - 大小写严格区分
        - 配对的标签必须一致
        
    - 命名空间
        - 为了防止命名冲突
              <Student type="web">
                  <Name>
                      haha
                  </Name>
                  <Age>
                       18
                  </Age>
              </Student>
              <Room>
                  <Location>
                        1-23-1
                  </Location>   
                        
                  <Name>
                        2014
                  </Name>
        - 如果归并上述内容信息，会产生冲突
        - 为了避免冲突，需要给可能冲突元素添加命名空间
        - xmlns：xml name space的缩写
            <Schooler xmlns:student="http://my_student" xmlns:room="http://my_room">
                <student:name>haha</Student:name>
                <room:name>2014</room:name>
                
# xml访问
## 读取
- xml读取分两个主要技术，SAX,DOM
- SAX(Simple API for XML):
    - 基于事件驱动的API
    - 利用SAX解析文档设计到解析器和事件两部分
    - 特点：
        - 快
        - 流式读取
        
- DOM 
    - 是w3c规定的XML编程的接口
    - 一个XML文件在缓存中以树形结构保存，读取
    - 用途
        - 定位浏览XML的任一节点信息
        - 添加删除相应内容
    - minidom
        - minidom.parse(filename):加载读取的xml文件，filename也可以是xml代码
        - doc.documentElement:获取xml文档对象，一个xml文件只有一个对应的文档对象
        - node.getAttribute(attr_name):获取xml节点的属性值
        。。。。
        案例v01
    - etree
        - 以树形结构来表示xml
        - root.getiterator:得到相应的可迭代的node集合
        - root.iter
        - find(node_name)：返回一个node_name的节点
        - root.findall(node_name):返回多个node_name的节点
        。。。。
        - 案例v02
        
- xml文件写入
    - 更改
        - ele.set:修改属性
        - ele.append：添加子元素
        - ele.remove：删除元素
        - 案例v03
    - 生成创建
        - SubElement 案例v04
        - minidom 写入  自己查资料
        - etree 创建    
         