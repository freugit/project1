
import requests

baseurl = "https://fanyi.baidu.com/sug"

data = {
    "kw":"girl"
}


rsp = requests.post(baseurl,data=data)

print(rsp.text)
print(rsp.json())

