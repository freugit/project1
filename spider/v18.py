"""
破解有道词典
v2
通过查找，找到js代码中的加密方法
1.这是计算salt的公式：salt = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
2.sign：n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!")
md5总共需要四个参数，第一个和第四个参数都是固定值的字符串，第三个是所谓的盐salt，第二个是需要翻译的单词
"""
from urllib import request,parse

def getSalt():
    """
    salt的公式是salt = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
    :return:
    """
    import time,random
    salt = int(time.time()*1000)+random.randint(0,10)
    return salt

def getMd5(v):
    import hashlib
    md5 = hashlib.md5()
    md5.update(v.encode("utf-8")) #update需要一个bytes格式参数
    sign = md5.hexdigest()
    return sign

def getSign(key,salt):
    sign = "fanyideskweb" + key + salt + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = getMd5(sign)
    return sign
def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    salt = str(getSalt())
    data = {
        "action": "FY_BY_REALTIME",
        "client": "fanyideskweb",
        "doctype": "json",
        "from": "AUTO",
        "i": key,
        "keyfrom": "fanyi.web",
        "salt": salt,
        "sign": getSign(key,salt),
        "smartresult": "dict",
        "to": "AUTO",
        "typoResult": "false",
        "version":"2.1"
    }
    data = parse.urlencode(data).encode()

    headers = {
                "Accept":"application/json, text/javascript, */*; q=0.01",
                "Accept-Language":"zh-Hans-CN, zh-Hans; q=0.8, en-US; q=0.5, en; q=0.3",
                "Cache-Control": "max-age=0",
                "Connection":"Keep-Alive",
                "Content-Length": len(data),
                "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"P_INFO=freulocvek@163.com|1530687078|2|163|11&22|gud&1530665121&163#gud&441900#10#0#0|134426&0|caipiao&163&epay&epay_client|freulocvek@163.com; OUTFOX_SEARCH_USER_ID_NCOO=587321170.8772837; OUTFOX_SEARCH_USER_ID=789884921@125.93.83.105; JSESSIONID=aaajD_OBlz16396vAJDww;___rl__test__cookies=1535947059279",
                "Host":"fanyi.youdao.com",
                "Origin":"http://fanyi.youdao.com",
                "Referer":"http://fanyi.youdao.com/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
                "X-Requested-With":"XMLHttpRequest"
    }

    req = request.Request(url=url,data=data,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)

if __name__ == "__main__":
    youdao("cannon")