from urllib import request,parse

"""
掌握对url进行参数编码的方法
需要使用parse
"""
if __name__=="__main__":
    url = "http://www.baidu.com/s?"
    wd = input("Input you keyword:")
    #要想使用date,需要使用字典结构
    qs = {"wd":wd}
    #转换url编码
    qs = parse.urlencode(qs)
    print(qs)
    fullurl = url+qs
    print(fullurl)
    #打开相应的url并把相应页面作为返回
    rsp = request.urlopen(fullurl)
    #把返回的结果读取出来
    #读取出来的内容类型为bytes
    html = rsp.read()
    html = html.decode()
    print(html)
