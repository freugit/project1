from urllib import request

if __name__ == "__main__":
    url = "https://www.163.com/"

    headers = {
        "Cookie":"__gads=ID=29c8879dedb0280b:T=1501223272:S=ALNI_MYv4AXLuyzDuaheHQMI1KbS97i5dg"
    }
    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode(encoding="gbk")
    with open("rsp.html","w") as f:
        f.write(html)