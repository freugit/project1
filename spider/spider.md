# 0. 爬虫的准备工作
- 参考资料
    - python网络数据采集，图灵工业出版
    - 精通python爬虫框架Scrapy，人民邮电出版社
    - [python3网络爬虫](http://blog.csdn.net/c406495762/article/details/72858983)
    - [Scrapy官方教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
- 前提知识
    - url
    - http协议
    - web前端 html，css，js
    - ajax
    - re，xpath
    - xml
    
# 1.爬虫简介
- 爬虫定义：网络爬虫（又被称为网络蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者）
是一种按照一定规则，自动地抓取万维网信息的程序或者脚本
另外一些不常用的名字还有蚂蚁，自动索引，模拟程序或者蠕虫
- 两大特征
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤：
    - 下载信息
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页上执行上两步内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）

- Python网络包简介
    - Python2.x:urllib,urllib2,urllib3,httplib,httplib2,requests
    - Python3.x:urllib,urllib3,httplib2,requests
    - Python2:urllib和urllib2配合使用，或者requests
    - Python3:urllib,requests

# 2.urllib
- 包含模块
    - urllib.request:打开和读取urls
    - urllib.error：包含urllib.request产生的常见的错误，使用try提取
    - urllib.parse:包含解析url的方法
    - urllib.robotparse:解析robots.txt文件
    - 案例v1
-  urlopen的返回对象,包含下列方法：
    - geturl()
    - info()
    - getcode()
- request.data 的使用
    - 访问网络的两种方法：
        - get:利用参数给服务器传递信息，参数为dict，然后用parse编码
            - 案例v3 
        - post：一般向服务器传递参数使用，post是自动加密处理，我们如果想使用post信息，需要用到data参数,
                使用post，意味着Http的请求头可能需要更改：
                - Content-Type:application/x-www.form-urlencode
                - Content-Length：数据长度
                - 简而言之，一旦更改请求方法，请注意其它请求头部信息相适应
            - urllib.parse.urlencode可以将字符转化为符合要求数据
            - 案例v4，
            - urlopen没有header参数，需要用request.Request
            - 案例v5
- URL Error的使用
    - URLError的产生原因：
        - 没网
        - 服务器链接失败
        - 找不到指定服务器
        - 是OSError的子类
        - 案例v6
    - HTTPError，是URLError的一个子类
        - 案例v7
    - 两者的区别：
        - HTTPError是对应的HTTP请求的返回码错误，如果返回的错误码是400以上的，则引发HTTPError
        - URLError对应的一般是网络出现问题，包括url问题
        - 关系区别：OSError-URLError-HTTPError
        
    - UserAgent 
        - UserAgent：用户代理：简称UA，属于headers的一部分，服务器通过UA来判断来访者身份
        - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问时抓包
            1.Android
            ...
            2.Firefox
            ...
            3.Google Chrome
            ...
            4.ios
            ...
            5.Edge
            Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134
            
        - 案例v8   
       
- ProxyHandler处理（代理服务器）
    - 使用代理IP，是爬虫的常用手段
    - 获取代理服务器的地址：
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问中，代理也不允许频繁访问某一个固定网站，所以代理一定要多        
    - 基本使用步骤：
        1.设置代理地址
        2.创建ProxyHandler
        3.创建Opener
        4.安装Opener
    - 案例v9
    
- cookie & session
    - 由于http协议的无记忆性，人们为了弥补这个缺憾，所采用的的一个补充协议
    - cookie是发放给用户（即http浏览器）的一段信息，session是保存在服务器上的对应的另一半信息，用来记录用户信息

- cookie和session的区别
    - 存放位置不同
    - cookie不安全
    - session会保存在服务器上一定时间，会过期
    - cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个
- session的存放位置
    - 存在服务器端
    - 一般情况下，session是放在内存中或者数据库中
    - 案例v10 ,没有cookie打开同一个网页返回的结果不同
- 使用cookie登录
    - 直接把cookie手动复制下来，放在请求头
        - 案例v11
    - http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
        - CookieJar
            - 管理存储cookie，向传出的http请求添加cookie
            - cookie存储在内存中，CookieJar实例回收后cookie得消失
        - FileCookieJar(filename,delayload = None,policy = None)
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar(filename,delayload = None,policy = None)
            - 创建于Mozilla浏览器cookie.txt兼容的FileCookieJar实例
        - lwpCookieJar
            - 创建于libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
        - 他们的关系是:CookieJar-->FileCookieJar-->MozillaCookieJar & lwpCookieJar
        - 利用cookiejar访问网络
            - 自动使用cookie登录，大致流程是
            - 打开登录页面后自动通过用户名密码登录
            - 自动提取反馈回来的cookie
            - 利用提取的cookie登录隐私页面
            - 案例v12
        - handler是Handler的实例，常用参数查看案例代码
            - 用来处理复杂请求
                - 生成cookie的管理器
                - cookie_handler = request.HTTPCookieProcessor(cookie)
                - 创建http请求管理器
                - http_handler = request.HTTPHandler()
                - 生成https管理器
                - https_handler = request.HTTPSHandler()
            - 创立handler后，使用opener打开，打开后相应的业务由相应的handler处理
            - cookie作为一个变量，打印出来看，案例v13
                - cookie的属性
                - name:名称
                - value:值
                - domain：可以访问此cookie的域名
                - path：可以访问此cookie的页面属性
                - expires：过期时间
                - size：大小
                - Http字段    
    - cookie的保存 --- FileCookieJar,案例v14
    - cookie的读取 --- 案例v15
    
- SSL
    - SSL证书就是指遵守SSL安全套接层协议的服务器数字证书（SecureSocketLayer）
    - 美国网景公司开发
    - CA（CertifacateAuthority）是数字证书认证中心，是发放、管理、废除数字证书的收信人的第三方机构
    - 遇到不信任的SSL证书，需要单独处理，案例v16
    
    
- js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是去md5值）
    - 经过加密，传输的就是密文，但是
    - 加密函数或者过程一定是在浏览器完成，也就是一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法，就可以模拟出加密过程，从而达到破解
    - 案例v17,v18
    
- ajax
    - 异步请求
    - 一定会有url，请求方法，可能有数据
    - 一般使用json格式
    - 案例，爬取豆瓣电影，案例v19
    
# Requests-献给人类
- HTTP for humans 更简洁更友好
- 继承了urllib所有的特征
- 底层使用的是urllib3
- 开源地址：https://github.com/requests/requests
- 中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
- 安装 conda install requests
- get请求
    - requests.get()
    - requests.request("get",url)
    - 可以带有headers和parmas参数
    - 案例v20
    
- get返回内容
    - 案例v21
    
- post
    - rsp = requests.post(url,data=data)
    - 案例v22
    - data,headers要求dict类型
    
- proxy
    - 代码示例： 
    proxies = {
    "http":"address of proxy"
    "https":"address of proxy"
    }
    rsp = requests.request("get",url,proxies=proxies)
    - 代理有可能报错，如果使用人数多，考虑安全问题，可能会被强行关闭

- 用户验证
    - 代理验证，代码示例：
            #可能需要使用HTTP basic Auth,可以这样
            proxy={"http":"china:123456@192.168.1.123:4444"}
            rsp = requests.get("http://www.baidu.com,proxies=proxy) 
        
    - web客户端验证
        - 如果遇到web客户端验证，需要添加auth=(用户名,密码)
            auth = ("test1","123456") #授权信息
            rsp = requests.get("http://www.baidu.com",auth=auth)
            
- cookie
    - requests可以自动处理cookie信息
            rsp = requests.get("http://xxxxxx")
            #如果对方服务器传送过来cookie信息，则可以通过反馈的cookies属性得到
            #返回一个cookiejar实例
            cookiejar = rsp.cookies
            
            #可以将cookiejar转换成字典
            cookiedict = requests.utils.dict_from_cookiejar(cookiejar)   

- session
    - 跟服务器端session不是一个东西
    - 模拟一次会话，从客户端浏览器链接服务器开始，到客户端浏览器断开
    - 能让我们跨请求保持一些参数，比如在同一个session实例发出的所有请求之间保持cookie   
            #创建session对象，可以保持cookie值
            ss = requests.session()
            headers = {"User-Agent":"xxxxx"}
            data = {"name":"xxxxx"}
            #此时，由创建的session管理请求
            ss.post("http://www.baidu.com",data=data,headers=headers)
            rsp = ss.get("xxxxxxx")
            
- https请求验证ssl证书
    - 参数verify负责表示是否需要ssl证书，默认是True
    - 如果不需要验证ssl证书，则设置成False表示关闭
            rsp = requests.get("https://www.baidu.com",verify=False)
            #如果用verify=True访问12306，会报错，因为证书有问题            



# 页面的解析和数据提取
- 结构化数据：先有结构，再谈数据
    - JSON文件
        - JSON Path
        - 转换成Python类型进行操作（JSON类）
    - XML文件
        - 转换成Python类型（xmltodict）
        - XPath
        - CSS选择器
        - 正则
- 非结构化的数据：先有数据，再谈结构
    - 文本
    - 电话号码
    - 邮箱地址
        - 通常处理此类数据，使用正则表达式
    - Html文件
        - 正则
        - XPath
        - CSS选择器
        
        
# 正则表达式
- 一套规则，可以在字符串文本中进行搜索替换等
- 案例v23 re的基本使用流程，match的基本使用
- 正则常用方法：
    - match:从开始位置开始查找，一次匹配
    - search:从任何位置查找，一次匹配
    - findall：全部匹配，返回列表
    - finditer:全部匹配，返回迭代器
    - split：分割字符串，返回列表
    - sub:替换
    - 案例v24 search使用
    - 案例v25 findall,finditer使用

- 匹配中文
    - 中文unicode的范围主要在[u4e00-u9fa5]
    - 案例v26

- 贪婪与非贪婪模式
    - 贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配
    - 非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配
    - python里面默认是贪婪模式
    - 例如：
        - 查找文本abbbbbbbcccc
        - re是 ab*
        - 贪婪模式结果是abbbbbbb
        - 非贪婪结果是a
        
# XML
- XML(EXtensibleMarkupLanguage)
- http://www.w3school.com.cn/xml/index.asp
- 案例v27.xml
- 概念：父节点、子节点、先辈节点、兄弟节点、后代节点

# XPath
- XPath(XML Path Language)，是一门在xml文档中查找信息的语言
- 官方文档：http://www.w3school.com.cn/xpath/index.asp
- XPath开发工具
    - 开源的XPath表达式工具：XMLQuire
    - chrome插件：XPath Helper
    - Firefox插件：XPath CHecker

- 常用的路径表达式：
    - nodename：选取此节点的所有子节点
    - /：从根节点开始选
    - //：选取元素，而不考虑元素的具体位置
    - .：当前节点
    - ..：父节点
    - @：选取属性
    - 案例:
        - bookstore:选取bookstore下面所有的子节点
        - /bookstore:选取根元素bookstore
        - bookstore/book：选取bookstore的所有为book的子元素
        - //book:选取book子元素
        - //@lang：选取名称为lang的所有属性
        
- 谓语(Predicates)
    - 谓语用来查找某个特定的节点，写在方括号中
    - /bookstore/book[1]：选取第一个属于bookstore下面叫做book的元素 
    - /bookstore/book[last()]：选取最后一个属于bookstore下面叫做book的元素
    - /bookstore/book[last()-1]：选取倒数第二个属于bookstore下面叫做book的元素
    - /bookstore/book[position()<3]：选取前两个属于bookstore下面叫做book的元素
    - /bookstore/book[@lang]：选取含有属性lang的属于bookstore下面叫做book的元素
    - /bookstore/book[@lang="cn"]：选取含有属性lang，且值为cn的属于bookstore下面叫做book的元素
    - /bookstore/book[@price < 90]：选取含有属性price，且小于90的属于bookstore下面叫做book的元素
    - /bookstore/book[@price<90]/title：选取含有属性price，且小于90的属于bookstore下面叫做book的元素下面的子元素title
- 通配符
    - *：任何元素节点
    - @*：匹配任何元素节点
    - node():匹配任意类型的节点
    
- 选取多个路径
    - //book/title | //book/author：选取book元素中的title和author元素
    - //title | //price：选取文档中的所有title和price元素

# lxml库
- python的HTML/XML的库
- 官方文档：http://lxml.de/index.html


- 功能：
    - 解析HTML 案例v28
    - xml文件读取，etree和XPath的配合使用，案例v29.py
    
# CSS选择器 BeautifulSoup4
- 现在使用BeautifulSoup4
- http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
- 几个常用工具提取信息比较：
    - 正则：很快，不好用，不需安装
    - beautifulsoup：慢，使用简单，安装简单
    - lxml：比较快，使用简单，安装一般
    
- 案例v30.py

- 四大对象
    - Tag
    - NavigableString
    - BeautifulSoup
    - Comment
- Tag
    - 对应Html中的标签
    - 可以通过soup.tag_name
    - tag两个重要的属性
        - name 
        - attrs
    - 案例v31.py

- NavigableString
    - 对应内容值，用法，soup.tag_name.string
    
- BeautifulSoup
    - 表示的是一个文档的内容，大部分可以把它当做tag对象
    - 一般我们可以用soup来表示
    
- Comment
    - 特殊类型的NavigableString对象
    - 对其输出，则内容不包括注释符号

- 遍历文档对象
    - contents：tag的子节点以列表的方式给出
    - children：子节点以迭代器形式返回
    - descendants：子孙节点
    - string
    - 案例v32 
    
- 搜索文档对象
    - find_all(name,attrs,recursive,text,**kwargs)
        - name:按照字符串搜索，可以传入的内容为：
            - 字符串
            - 正则表达式
            - 列表
        - kwargs参数：可以用来表示属性
        - text：对应tag的文本值
        - 案例v32
        
- css选择器
    - 使用soup.select，返回一个列表
    - 通过标签名称：soup.select("title")
    - 通过类名：soup.select(".content")
    - id查找：soup.select("#name_id")
    - 组合查找:soup.select("div #input_content")
    - 属性查找：soup.select("img[class='photo']")
    - 获取tag内容：tag.get_text
    - 案例v33
    
# 动态HTML
## 爬虫和反爬虫
## 动态HTML介绍
- JavaScript
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从JavaScript代码入手采集
    - Python第三方库运行JavaScript，直接采集你在浏览器看到的页面
## Selenium+PhantomJS
- Selenium：web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装：pip install selenium=2.48.0
    - 官网：http://selenium-python.readthedocs.io/index.html
    
- PhantomJS(幽灵)
    - 基于WebKit的无界面浏览器
    - 官网：http://phantomjs.org/download.html
- Selenium 库有一个WebDriver的API
- WebDriver可以跟页面上的元素进行各种交互，用它可以来进行爬取
- 案例v34
- chrome + Chromedriver
    - 下载安装chrome
    - 下载安装chromedriver
- Selenium操作主要分两大类：
    - 得到 UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionChains来做到
    - 案例v35
   
 # 验证码问题
 - 验证码：防止机器人或爬虫
 - 分类：
    - 简单图片
    - 极验，官网www.geetest.com
    - 12306
    - 电话
    - google验证
    
 - 验证码破解：
    - 通用方法：
        - 下载网页和验证码
        - 手动输入验证号码
    - 简单图片
        - 使用图像识别软件或者文字识别软件
        - 可以使用第三方图像验证码破解网站，www.chaojiying.com
    - 极验
        - 破解比较麻烦
        - 可以模拟鼠标等移动
        - 一直在进化
    
    - 12306
    - 电话
        - 语音识别
    - google验证
 # Tesseract
- 机器视觉领域的基础软件
- OCR:OpticalCharacterRecognition 光学文字识别
- Tesseract:一个OCR库，由google赞助
- 案例v36   
 
    
      
