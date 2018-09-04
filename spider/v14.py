from urllib import request,parse
from http import cookiejar
#创建cookiejar实例
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)

#生成cookie的管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
#创建http管理器
http_handler = request.HTTPHandler()
#生成https的管理器
https_handler = request.HTTPSHandler()
#创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handle)

def login():
    """
    负责初次登陆
    需要输入用户名密码，用来获取登陆cookie凭证
    :return:
    """
    #此url 需要从登陆form的aciton属性中提取
    url = "http://www.renren.com/PLogin.do"

    #此键值需要从登陆form的两个对应input中提取name属性
    data = {
        "email":"13119144223",
        "password":"123456"
    }
    data = parse.urlencode(data)
    req = request.Request(url,data = data.encode())
    rsp = opener.open(req)
    #保存cookie到文件
    #ignore_discard表示即使cookie将要被丢弃也要保存下来
    #ignore_expires表示如果该文件中cookie即使已经过期，也保存下来
    cookie.save(ignore_discard=True,ignore_expires=True)

if __name__ == "__main__":
    """
    123
    """
    login()
