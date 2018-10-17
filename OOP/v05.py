import json


student = {
    "name":"liudana",
    "age":18,
    "mobile":"15512231222"
}

print(type(student))

stu_json = json.dumps(student)
print(type(stu_json))

print("JSON对象：{0}".format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)

