# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 18:02
# @Author  : Dawn Lee
# @Email   : lisantao_tao@outlook.com
# @File    : mysql.py
# @Software: PyCharm

import pymysql

#连接数据库
db = pymysql.connect("localhost","root","1234567890","Spring")

#使用cursor()方法创建一个游标对象
cursor = db.cursor()

#使用execute()方法执行SQL语句
cursor.execute("SELECT * FROM article")

#使用fetall()获取全部数据
data = cursor.fetchall()

#打印获取到的数据
print(data)

#关闭游标和数据库的连接
cursor.close()
db.close()



