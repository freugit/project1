from urllib import request

if __name__=="__main__":
    url = "http://tech.163.com/18/0723/01/DNC3F97200097U7S.html"
    #打开相应的url并把相应页面作为返回
    rsp = request.urlopen(url)
    #把返回的结果读取出来
    #读取出来的内容类型为bytes
    print(type(rsp))
    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))