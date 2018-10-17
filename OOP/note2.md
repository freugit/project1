# JSON
- 在线工具
    - https://www.sojson.com
    - http://www.w3school.com.cn/json/
    - http://www.runoob.com/json/json-tutorial.html
    
- JSON(JavaScriptObjectNotation)
- 轻量级的数据交换格式，基于ECMAscript
- JSON格式是一个键值对形式的数据集
    - key:字符串
    - value:字符串，数字，列表，json
    - json使用大括号包裹
    - 键值对直接用逗号隔开
    
        student = {
            "name":"wangdapeng"
            "age":18
            "mobile":13423332221
            }
- json和python的格式对应
    - 字符串：字符串
    - 数字：数字
    - 队列：list
    - 对象：dict
    - 布尔值：布尔值
    
- python for json
    - json包
    - json和python对象的转换
        - json.dumps():对数据编码，把python格式表示成json格式
        - json.loads():对数据解码，把json格式转换成python格式
    - python读取json文件
        - json.dump():把内容写入文件
        - json.load():把json文件内容读入python
        - 案例 v05 v06     
    
# 正则表达式(RegularExpression,re)
    - 是一个计算机科学的概念
    - 用于使用单个字符串来描述，匹配符合某个规则的字符串
    - 常常用来检索，替换某些模式的文本
# 正则的写法
    - .(点号)：表示任意一个字符，除了\n，比如查找所有的字符\.
    - []:匹配中括号列举的任意字符，比如[L,Y,0]，LLY,Y0可以,LIU不行
    - \d:任意一个数字
    - \D:除了数字都可以
    - \s:表示空格，tab键
    - \S:除了空格都可以
    - \w:英文字母和数字和下划线，就是a-z,A-Z,0-9,_
    - \W:除了英文字母和数字和下划线
    - *:表示前面内容重复零次或多次，\w*
    - +:表示前面内容至少出现一次
    - ？：前面内容零次或一次
    - {m,n}:允许前面内容出现最少m次，最多n次
    - ^:匹配字符串的开始
    - $:匹配字符串的结尾
    - \b:匹配单词的边界
    - ():对正则表达式内容进行分组，从第一个括号开始，编号逐渐增大
    
        验证一个数字：^\d$
        必须有一个数字，最少一位：^d+$
        只能出现数字，且位数为5到10位：^d{5,10}$
        只能输入英文字符和数字:^[A-Za-z0-9]$
        验证qq号码:[0-9]{5,12}
        
    - \A:只匹配字符串开头，\Aabcd,则abcd
    - \Z:仅匹配字符串末尾，abcd\Z,abcd
    - |:左右任意一个
    - (?P<name>...):分组，除了原来的编号再指定一个别名，(?P<id>12345){2}
    - (?P=name):引用分组
    
    
# XPath
- 在XML文件中查找信息的一套规则/语言，根据XML的元素或属性进行遍历
- http://www.w3school.com.cn/xpath/index.asp
# XPath 开发工具
- 开源的XPath表达式编辑工具：XMLQuire
- Chrome插件，XPath Helper
- Firefox插件:XPath Checker

# 选取节点
- nodename:选取此节点的所有子节点
- / 从根节点开始选取
    /Student 选取根元素Student，如果根不是Student，则没有结果
- // 选取节点，不考虑它的位置
    //age 选取所有age的节点，组成列表返回
    
- . 选取当前的节点
- .. 选取当前节点的父亲节点
- @ 选取属性
- XPath中查找一般按照路径方法查找，以下是路径的表示方法
    School/Teacher 返回Teacher节点
    School/Student 返回Student节点
    //Student 选取所有Student的节点，不考虑位置
    School//Age 选取School下面所有的Age节点
    //@Other 选取Other属性
    //Age[@Detail] 选取带有属性Detail的Age元素
    
# 谓语 - Predicates
- /School/Student[1]:选取School下面的第一个Student节点
- /School/Student[last()]选取School下面的最后一个Student节点
- /School/Student[last()-1]选取School下面的倒数第二个Student节点
- /School/Student[position()<3]选取School下面的前面二个Student节点
- //Student[@score] 选取带有属性score的Student的节点
- //Student[@score="99"]选取带有属性score并且属性值是99的Student节点
- //Student[@score]/Age 选取带有属性score的Student节点的子节点Age

# XPath的一些操作
- 或者  |
    //Student[@score]|//Teacher 选取带有属性score的Student节点和Teacher节点
    
- 其余不常见的XPath运算符号 + - * div 等等

# 网络编程
- 网络
- 网络协议：一套规则
- 网络模型
    - 七层模型
        - 物理层
        - 数据链路层
        - 网络层
        - 传输层
        - 会话层
        - 表示层
        - 应用层
    - 四层模型 - 实际应用
        - 链路层
        - 网络
        - 传输层
        - 应用层
- 每一层都有相应的协议负责交换信息或者协同工作
- TCP/IP 协议族
- IP地址：负责在网络上的唯一定位一个机器
    - IP地址分ABCDE类
    - 是由四个数字段组成，每个数字的取值是0-255
    - 192.168.xxx.xxx局域网IP
    - 127.0.0.1本机
    - IPv4,IPv6
    
    
- 端口 
    - 范围：0-65535
        - 知名端口：0-1023
        - 非知名端口：1024-65535
        
- TCP/UDP协议
- UDP:非安全的不面向链接的传输
    - 安全性差
    - 大小限制64kb
    - 没有顺序
    - 速度快
- TCP
    - 基于链接的通信  

- SOCKET编程
    - socket（套接字）：是一个网络通信的端点，能实现不同主机的进程通信，网络大多基于socket完成通信
    - 通过IP+端口定位对方并发送消息的通信机制
    - 分为UDP和TCP
    - 客户端Client:发起访问的一方
    - 服务器端Server：接受访问的一方
- UDP 编程
    - Server端流程：
        1.建立通信的socket
        2.绑定，为创建的socket指派固定的端口和ip地址
        3.接受对方发送内容
        4.给对方发送反馈，此步骤为非必须步骤
    - Client端流程：
        1.建立通信的socket
        2.发送内容到指定服务器
        3.接受服务器给定的反馈内容
    - 案例 服务器端s01 客户端s02
    - 服务器程序要求永久运行，一般用死循环处理
    - 改造的服务器版本 s03
- TCP编程
    - 面向链接的传输，即每次传输之前需要先建立一个链接
    - 客户端和服务器端两个程序需要编写
    - Server端的编写流程：
        1.建立socket负责具体通信，这个socket其实只负责接受对方的请求
        2.绑定端口和地址
        3.监听接入的访问socket
        4.接受访问的socket，可以理解接受访问建立了一个通信的链路通路
        5.接受对方的发送内容，利用接收到的socket接收内容
        6.如果有必要，给对方发送反馈信息
        7.关闭链接通路
     
    - Client端流程：
        1.建立通信socket
        2.链接对方，请求跟对方建立通路
        3.发送内容到对方服务器
        4.接受对方的反馈
        5.关闭链接通路
    
    - 案例s04，s05  
# FTP 编程
    - FTP（FileTransferProtocal）文件传输协议
    - 用途：定制一些特殊的上传下载文件的服务
    - 用户分类：登陆FTP服务器必须有一个账号
        - Real账号：注册账户
        - Guest账户：可能临时对某一类人的行为进行授权
        - Anonymous账户：匿名账户，允许任何人

- FTP工作流程
    1.客户端连接远程服务器上的FTP服务器
    2.客户端输入用户名和密码（或者"anonymous"和电子邮件地址）
    3.客户端和服务器进行各种文件传输和信息查询操作
    4.客户端从远程FTP服务器退出，结束传输

- FTP文件表示：
    - 分三段表示FTP服务器上的文件
    - HOST：主机地址，类似于ftp.mozilla.org,以ftp开头
    - DIR：目录，表示文件所在本地的路径，例如pub/android/forcus/1.1
    - File:文件名称，例如 Kr1.1.apk
    - 如果想完整精确表示ftp上一个文件，需要把三部分结合在一起
    - 案例 s06

# Mail编程
## 电子邮件的历史
- 起源
    - 1969 Leonard K. 教授发给同事的"LO"
    - 1971 美国国防部自主的阿帕网（Arpanet）的通讯机制
    - 通讯地址里用@
    - 1987年中国的第一份电子邮件
    "Across the Great Wall we can reach every corner in the world"
    
- 管理程序
    - Euroda使邮件普及
    - Netscape，outlook，foxmail后来居上
    - Hotmail使用浏览器发送邮件
    
- 参考资料
    - 【官网】（https://docs.python.org/3/library/email.mime.html）

## 邮件工作流程
- MUA（MailUserAgent）邮件用户代理
- MTA（MailTransferAgent）邮件传输代理
- MDA（MailDeliveryAgent）邮件投递代理

- laoshi@qq.com 老师，北京海淀
- xuesheng@sina.com 学生，上海江岸区

- 流程
    1.MUA->MTA, 邮件已经在qq服务器上
    2.qq MTA -> sina MTA,邮件在新浪的服务器上
    3.sina MTA -> sina MDA 此时邮件已经在你的邮箱里了
    4.sina MDA -> MUA(foxmail/outlook) 邮件下载到本地电脑
    
- 编写程序
    - 发送：MUA -> MTA with SMTP：SimpleMailTransferProtocal
    - 接收：MDA -> MUA with POP3 and IMAP:PostOfficeProtocal v3 and ...
- 准备工作
    - 注册邮箱（以qq邮箱为例）
    - 第三方邮箱需要特殊设置，以qq邮箱为例
        - 进入设置中心
        - 取得授权码
- Python for mail
    - SMTP协议负责发送邮件
        - 使用email模块构建邮件
            - 纯文本邮件
            - 案例s07
        - HTML格式邮件发送
            - 准备HTML代码作为内容
            - 把邮件的subtype设为HTML
            - 发送
            - 案例s08
        - 发送带附件的邮件
            - 可以把邮件看作是一个文本邮件和一个附件的合体
            - 一封邮件如果涉及多个部分，需要使用MIMEMultipart格式构建
            - 添加一个MIMEText正文
            - 添加一个MIMEBase或者MIMEText作为附件
            - 案例s09
        - 添加邮件头，抄送等信息
            - mail["From"] 表示发送者信息，包括姓名和邮件
            - mail["To"]表示接收者信息，包括姓名和邮件地址
            - mail["Subject"]表示摘要等信息
            - 案例s10   
        - 同时支持html和text格式
            - 构建一个MIMEMultipart格式邮件
            - MIMEMultipart的subtype设置成alternative格式
            - 添加HTML和text邮件
            - 案例s11
        - 使用smtplib模块发送邮件
        
    - POP3协议接收邮件
        - 本质上是MDA到MUA的一个过程
        - 从MDA下载下来的是一个完整的邮件结构体，需要解析才能得到每个具体内容
        - 步骤
            1.用poplib下载邮件结构体的原始内容
                1.准备相应的内容（邮件地址，密码，POP3实例）
                2.身份认证
                3.一般会先得到邮箱内的整体列表
                4.根据相应序号，得到某一封信的数据流
                5.利用解析函数进行解析出相应的邮件结构体
           2.用email解析邮件的具体内容
        - 案例s12
# HTTP
- 超文本（HyperText）
    - 包含有超链接和各种多媒体元素标记（Markup）的文本，这些超文本彼此链接
    形成网状（Web），因此又被称为网页（WebPage），这些链接使用URL表示，最常见的超文本
    格式是HTML
    
- URL（UniformResourceLocator）
    - 用来唯一标识万维网中的某一个文档，由协议、主机和端口（默认80）以及文件名三部分组成，如：
    http://www.sxtyu.com:80/news/index.html
    
- HTTP协议
    - 请求/响应模式 GET index/html
    - 持久链接和非持久链接
    - 无状态性，是指同一个客户端第二次访问web服务器上的页面时，服务器无法知道这个客户端曾经访问过
    
- HTTP报文结构
    - 请求报文，从客户端向web服务器发送的请求报文，报文的所有字段都是ASCII码，由CRLF回车换行
        - 请求行 GET /index.html HTTP/1.1
        - 首部行 用来说明浏览器 服务器或报文主体的一些信息，行间用CRLF回车换行，如：Host: www.sxtyu.com Connection: close User-Agent： Mozilla/5.0 Accept-Language： cn
        - 两个CRLF回车换行后，即一个空行后是实体主体
    - 应答报文，从服务器端返回客户端的报文，所有字段都是ASCII码
        - 状态行，如:HTTP://1.1 200 OK
        - 首部行，同上，如：Date: Wed,08 May 2008 22  Server: Apache/1.3.2(Unix)
        - 两个CRLF回车换行后，即一个空行后是实体主体，实体是返回的内容，如页面等等
        
    - 请求报头的方法有：
        - GET 请求读取一个Web页面
        - HEAD 请求读取一个Web页面的首部
        - POST 附加一个命名资源（如Web页面）
        - PUT 请求存储一个Web页面
        - DELETE 删除Web页面
        - TRACE 用于测试，要求服务器送回收到的请求
        - CONNECT 用于代理服务器
        - OPTION 查询特定选项
        上述方法是HTTP协议规定的方法，可以不实现，也可以定义自己的方法
    - 响应报文的状态码：
        - 1xx  通知信息 100=服务器正在处理客户请求
        - 2xx  成功    200= 请求成功（OK）
        - 3xx  重定向   301=页面改变了位置
        - 4xx  用户错误  403= 禁止的页面；404=页面未找到
        - 5xx  服务器错误  500=服务器内部错误，503=以后再试
        - 具体各状态码的含义，请参考：http://www.w3.org/Protocols/rfc2616/rfc2616.html
    - 首部行字段名HTTP其中的一些规定如下：
        - User-Agent：类型：请求，关于浏览器和它平台的信息，如：Mozilla5.0
        - Accept    类型：请求，客户端处理的页面的类型，如text/html
        - Accept-Charset 类型：请求，客户端可以接受的字符集，如：Unicode-1.1
        - Accept-Encoding 类型：请求，客户端能处理的页面编码方法，如gzip
        - Accept-Language 类型：请求，客户端能处理的语言，如en（英语），zh-cn（简体中文）
        - Date 类型：双向，消息发送时的日期和时间
        - Server 类型：响应，服务器的相关信息
        - Content-Encoding 类型：响应，内容是如何被编码的，如gzip
        - Content-Language 类型：响应，页面使用的自然语言
        - Content-Length 类型：响应，以字节计算的页面长度
        - Content-Type 类型：响应，页面的MIME类型
        - Location 类型：响应，指示客户将请求发送给别处，即重定向到另一个URL
        - set-Cookie 类型：响应，服务器希望客户保存一个Cookie
        
- HTTP代理