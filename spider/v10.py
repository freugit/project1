from urllib import request
if __name__ == "__main__":
    url = "https://www.163.com/"
    rsp = request.urlopen(url)
    html = rsp.read().decode(encoding="gbk")

    with open("rsp.html","w") as f:
        f.write(html)