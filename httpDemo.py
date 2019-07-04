import http.client

import urllib,parser
#初始化一个http链接
conn = http.client.HTTPConnection("www.python.org")

#指定请求方式和请求的链接地址
conn.request("GET","/doc/")

#返回得到的http response
res = conn.getresponse()
#打印状态码
print(res.status,res.reason)
#打印请求头
print(res.getheaders())
#打印body部分
print(res.read())
#如果链接未关闭则打印前两百个字节
if not res.close():
    print(res.read(200))
#链接关闭
conn.close()
#重新请求
conn.request("GET","/parrot.spam")
#得到请求内容
res1 = conn.getresponse()
#打印状态码
print(res1.status,res1.reason)
#关闭连接
conn.close()