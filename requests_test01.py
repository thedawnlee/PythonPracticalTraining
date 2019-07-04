#网页请求函数

import requests

r = requests.get("http://www.baidu.com")

print(type(r))

print(r.text())