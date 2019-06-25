#day8 
<h2>PYSQL

    connect关键参数：
        host  
        post=3306  
        username  
        password  
        databasename
###操作实例：
        
        
        import pymysql


        db =  pymysql.connect('localhost','root','','mysql')
        
        
        cursor = db.cursor()
        
        
        cursor.execute("select version()")
        
        
        data = cursor.fetchall()
        print(data)
        
        cursor.close()
        db.close()
<h2>Dbutil for python
    
    import pymysql
    class DBUtil:
        def __init__(self,localhost = 'localhost',username='root',password='',databasename='rg01'):
            self.db = pymysql.connect(localhost,username,password,databasename)
            self.cursor = self.db.cursor()
        #获取连接对象
        def get_db(self):
            return self.db
        #获取游标对象
        def get_cursor(self):
            return self.cursor
        #关闭链接
        def close_connection(self):
            if self.cursor is None:
                self.cursor.close()
            if self.db is None:
                self.db.close()
        #findall方法
        def Listall(self,tablename):
            sql = "select * from "+tablename
            print(sql)
            self.cursor.execute(sql)
            listall = self.cursor.fetchall()
            self.close_connection()
            return listall
        #通过ID查找
        def findById(self,tablename,column,value):
            sql = "select * from "+tablename+" where "+column+" = %d"%(value)
            print(sql)
            self.cursor.execute(sql)
    
            data = self.cursor.fetchall()
            self.close_connection()
            return data
        #插入数据
        def insetOne(self,sql,params):
            res = 0
            try:
                res = self.cursor.execute(sql,params)
                #self.cursor.execute(sql)
                self.db.commit()
    
            except (Exception):
                print('ERROR')
    
                self.db.rollback()
            finally:
                self.close_connection()
                if res ==1:
                    print("插入成功")
        #按ID删除
        def deleteOneById(self,tableName,colunm,value):
            res = 0
            sql = "delete from "+tableName+" where "+colunm+" = %d"%(value)
            try:
                res = self.cursor.execute(sql)
                self.db.commit()
            except:
                print('ERROR')
                self.db.rollback()
            finally:
                self.close_connection()
                if res==1:
                    print("删除成功")
        #更新方法
        def update(self,sql):
            res = 0
            try:
                res =self.cursor.execute(sql)
                self.db.commit()
            except:
                print('ERROE')
                self.db.rollback()
            finally:
                self.close_connection()
                if res==1:
                    print("更新成功")
                elif res==0:
                    print("更新失败")
        #获取记录条数
        def get_count(self,tablename):
            sql = 'select count(*) from '+tablename
            self.cursor.execute(sql)
            count = self.cursor.fetchone()[0]
            self.close_connection()
            return count
        #通过自定义SQL删除
        def deleteBySql(self,sql):
            res = 0
            try:
                res = self.cursor.execute(sql)
                self.db.commit()
            except:
                print('ERROR')
                self.db.rollback()
            finally:
                if res==1:
                    print("删除成功")
                elif res==0:
                    print("删除失败")
                self.close_connection()
        #获取具有相同属性的记录的总条数
        def get_OneColumn_Count(self,tableName,column,value):
            sql = "select count(*) from "+tableName+" where "+column+"="+value
            print(sql)
            self.cursor.execute(sql)
            count = self.cursor.fetchall()[0][0]
            self.close_connection()
            return count
        获取具有多个相同属性的记录总条数
        def get_ManyColunm_Count(self,tableName,colunm1,value1,colunm2,value2):
            sql = "select count(*) from "+tableName+" where "+colunm1+" = "+value1+" and "+colunm2+" = "+"'"+value2+"'"
            print(sql)
            self.cursor.execute(sql)
            count = self.cursor.fetchall()
            self.close_connection()
            return count
        #获取主键最大值
        def getMaxId(self,tableName):
            sql = "select max(id) from "+tableName
            self.cursor.execute(sql)
            return self.cursor.fetchall()[0][0]


<h2>html面试关键标签

        <form> 
        <table>
        <a>标签
        锚点实现返回顶部操作
        <ol><ul>
        <div>


<h2>SOCKET套接字客户端编程  
实例：

    服务器代码：
    import socket

    import  sys
    
    socketServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    
    host = socket.gethostname()
    
    port = 9999
    
    socketServer.bind((host,port))
    
    socketServer.listen(5)
    while True:
        #建立客户端连接
        clientsocket, addr =socketServer.accept()
    
        print("连接地址：%s" % str(addr))
        msg ="Welcome to XXX"
        clientsocket.send(msg.encode('utf-8'))
        clientsocket.close()

    客户端代码：
    import sys
    import  socket
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    
    host = socket.gethostname()
    
    port  = 9999
    
    
    s.connect((host,port))
    
    msg = s.recv(1024)
    
    s.close()
    
    print(msg.decode('utf-8'))


<h2>http编程实例  
    
    
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
