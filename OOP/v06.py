import json

data = {"name":"hahaho","age":12}

with open("t.json","w") as f:
    json.dump(data,f)

with open("t.json","r") as f:
    d = json.load(f)
    print(d)
