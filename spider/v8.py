"""
访问一个网址
更改自己的UserAgent进行伪装
"""

from urllib import request,error

if __name__ =="__main__":
    url = "http://www.baidu.com"
    try:
        #使用headers伪装UA,也可以用Request实例的add_header方法，第一个参数是UserAgent，第二个是值
        headers = {}
        headers["UserAgent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
        req = request.Request(url,headers=headers)

        #正常访问
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

    print("Done....")