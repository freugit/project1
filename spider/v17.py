"""
破解有道词典
v1 不成功
"""
from urllib import request,parse

def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "action": "FY_BY_REALTIME",
        "client": "fanyideskweb",
        "doctype": "json",
        "from": "AUTO",
        "i": "girl",
        "keyfrom": "fanyi.web",
        "salt": "1535947059298",
        "sign": "bf7e9e2d482b90dfdfc5fbe2fcd43c18",
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
                "Content-Length": "200",
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
    youdao("girl")