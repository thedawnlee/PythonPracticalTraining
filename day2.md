<h1>实训day2

---


##冒泡算法

>>设计思路：
>>>两层for循环嵌套每轮循环跳出最大值然后剔除这个最大项将剩余的len（a）-1项进行继续筛选，直到循环结束，排序完成。    
####程序代码    
    in：
    a = [9,8,7,6,5,4,3,2,1]
    for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if(a[j]>a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
    
    
    out：
    [1, 2, 3, 4, 5, 6, 7, 8, 9]



<h2>函数式编程

    小括号不能省略   
    高内聚低耦合   
    冒号和缩进来表示同一个代码段  
    定义函数


###参数传递
    
    
    可变类型：
        与不可变类型相反
    exp:
    in: 
    def change(mylist):
        mylist.append([1,23,4])
        print('func取值',mylist)
        return mylist
        num = [1]
    
    change(num)
    print(num)
    
    out:
    func取值[1, [1, 23, 4]]
    [1, [1, 23, 4]]

    不可变类型：
        传递的只是a的值
        对a本身没有任何影响
        只是修改另一个复制对象a的值
        
###return语句
    
    
    代表函数的结束
    如果不加return可以用不同的缩进来替代
    可以返回多个参数
    要用多个数字来接受返回的处理结果
    

###变量的作用域  
    
    
    全局变量
    局部变量
    优先推荐使用局部变量
    函数结束以后，局部变量会被删除
    exp：
    a = 3
    def test(x):
        a = x+5
        return x
    test(a)
    print(a)   
    
    out:
    a = 3
    a 与 函数内的a 作用域不同 
    exp2:
    in:
    def demo():
    global x 
    x = 3
    y = 4
    print(x,y)
    x = 5
    demo()
    out:
    x = 3
    y = 4
    
    
<h2>面向对象与面向过程
<h3>面向对象的三个基本特征  
多态 封装 继承  
python中都默认继承了object类
    

<h4>self变量
    
    self参数要放在类内方法的参数的首位
    相当于类本身

<h4>构造器方法

    创建对象之初就带有某些属性，通过一个__init__函数来进行赋值
    exp:
    class Complex():
    def __init__(self,real,image):
        self.r = real
        self.i = image

    c = Complex(10,5)      
    print(c.i,c.r)
    out:
    5,10
    



<h4>超类
    
    将所有类中共有的部分提出来作为共有属性
    基类就是抽象多个共同的属性得到一个类

<h4>私有化
    
    类中方法加上下划线，代表方法私有
    私有化属性的调用
    class people:
        name = ''
        age  =0
        __weight = 0
        def __init__(self,n,a,w):
            self.name = n
            self.age  = a
            self.weight = w
        def speak(self):
            print("%s 说：我%d 岁"%(self.name,self.age))
        def get_weight(self):
            return self.weight
    c = people('a',12,12)
    c.speak()
    out1:a 说：我12 岁
    c.weight
    out2:12
    
<h3>单例模式 singleton

    单例模式
    全局中只存在一个实例，不允许存在更多的实例
    实现步骤：
    1.__new__方法
    2.__init__方法 初始化 定义属性
<h4>操作实例(new方法)：

    in：
    class MusicPlay():
        instance = None
        def __new__(cls, *args, **kwargs):
            if cls.instance is None:
                print("s")
                cls.instance = super().__new__(cls)
                return cls.instance
            else:
                return cls.instance
        def __init__(self):
            print("初始化!")


    c = MusicPlay()
    d = MusicPlay()
    
    print(id(c))
    print(id(d))
    
    out：
    s
    初始化!
    初始化!**执行了2次
    4375100720
    4375100720

<h4><h4>操作实例(init方法)：
    
    class MusicPlay():
        instance = None
        init_flag = False
        def __new__(cls, *args, **kwargs):
            if cls.instance is None:
                print("s")
                cls.instance = super().__new__(cls)
                init_flag  = True
                return cls.instance
            else:
                return cls.instance
        def __init__(self):
            if MusicPlay.init_flag is False:
                print("初始化!")
                MusicPlay.init_flag = True
                return
            else:
                return

    c = MusicPlay()
    d = MusicPlay()
    
    print(id(c))
    print(id(d))

    out:
    s
    **初始化!**只执行了一次
    140708028522336
    140708028522336


<h3>Python的异常
    
    Python中存在两种错误：语法错误和异常
    语法错误：也称之为解析错误，红波浪线 syntaxError
    异常：运行期间的错误
    解决方案：1.抛出 2.捕获
    
    try:
    i = 1
    a = i/0
    except Exception:
        print('error')
    finally:
        print("finally")
    
    
    
    try:

    #11/0

    open("xxx.txt")

    print(num)

    print("------1------")

    except(NameError,FileNotFoundError):
    
        print('如果捕获到异常后作处理')
    
    except Exception as ret:
    
        print("如果采用Exception那么意味着只要上面没有捕获到的，在这里的都会捕获到"+ret)
    
    finally:
    
        print('异常捕获结束')
    
    ​
    out：
    如果捕获到异常后作处理
    异常捕获结束


<h3>双重异常捕获
    
    
    import time
    try:
        f = open('test.txt')
        try:
    
            while True:
                content  = f.readline()
                if len(content)==0:
                    break
                time.sleep(2)
                print(content)
        except:
            pass
        finally:
            f.close()
            print("关闭资源")
    except:
        print("1")

<h3>异常传递
<h3>抛出自定义异常
    
    语法没有问题
    但是逻辑上存在问题
    class databaseException(Exception):
        def __init__(self,err='自定义异常'):
            Exception.__init__(self,err)
    
        def testRaise():
            raise databaseException()
        try:
            testRaise()
        except databaseException as e:
            print(e)
     out:
     自定义异常
<h2>数据库 
<h3>数据库语言的分类
    
    DQL 数据库查询语言 查
    DML 数据库操作语言 增删改
    DDL 数据库定义语言 定义表、数据库
    DCL 数据库控制语言 是用来设置或更改数据库用户或角色权限的语句，包括（grant,deny,revoke等）语句。这个比较少用到
<h4>DDL
    
    查看数据库 show databases
    创建数据库 create database if not exists tablename
    删除表    drop table tablename
    查看表结构  desc tablename
    
<h4>完整性约束
    
    mysql:
    主键 外键 非空 唯一 主键自增
    oracle：
    主键 外键 非空 唯一 check 
    
    主键自带 非空and唯一 特性
    

    
-----
Date：2019.06.19  
Author:Dawn  
Location:Jinan   
Wechat：llmllm_llm  
>>[新浪微博](https://weibo.com/u/5034954422)
![AI](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=761154721,3108771239&fm=26&gp=0.jpg "区块链")
