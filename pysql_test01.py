import pymysql

#DDL操作
import Db_Util as db

db.cursor.execute("drop table if exists emp")



sql = '''create table emp(

empno int(4) not null ,
ename varchar(20) default null,
job varchar(20) default  null ,
mgr int(4) default  null ,
hiredate date default null)
'''
db.cursor.execute(sql)


db.cursor.close()

db.db.close()

