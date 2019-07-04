# import requests
# from bs4 import  BeautifulSoup
#
# r = requests.get("http://www.baidu.com")
#
# r.encoding = "utf-8"
#
# soup = BeautifulSoup(r.text)
#
# print(type(soup))
# print(soup.head)
#
# print(soup.title)
# print("-----------------------------")
# print(soup.a)
#
# print(soup.a.name)
#
# print(soup.a.attrs)
#
# print("=========================")
#
# title = soup.title
#
# print(title.string)
#
# a = soup.find_all('a')
#
# print(len(a))
#
# print(soup.find_all('script'))
#
# print(soup.find_all('script', {'src': "http://www.zgxiangxin.com/jquery/jquery-1.10.4.min.js"}))
#
# import  re
#
# print(soup.find_all("script", {'src': re.compile('jquery')}))
#
#
#
#



import Db_Util as db

#
conn = db.DBUtil(password='12345',databasename='rkrank')
#
#
# conn.insetOne("insert into rkrank01 values(%s,%s,%s,%s,%s,%s,%s,%s)",('1', '麻省理工学院', '360.5', '72.4', '79.5', '70.6', '94.5', '100.0'))


sql = "insert into rkrank01 values("+7*"%s,"+"%s"+")"
print(sql)
conn.insetOne(sql,('1', '麻省理工学院', '360.5', '72.4', '79.5', '70.6', '94.5', '100.0'))
