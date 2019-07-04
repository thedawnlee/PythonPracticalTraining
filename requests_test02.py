import requests

r = requests.get("http://www.baidu.com")

print(r.status_code)

print(r.text)

print(r.encoding)


r.encoding='utf-8'

print(r.text)

s = requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg=天气深圳")

print(s.text)




