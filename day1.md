<h1>实训day1

<h2>列表操作  


####数组的定位
    a  = [[1,2],[3,4],[5,6]]  
#####in:  
    a[0][0]  
#####out:
    [1,2]


####pop方法 删除最后一个元素

    a.pop()
    
    print(a)
####pop方法删除指定位置元素
    a.pop(1)
    
    print(a)

####remove pop del
    
    a.remove([1,2])
    
    del(a)



####index 定位
    a  = [[1,2],[3,4],[5,6]]
    
    print(a[2])
    

####切片 操作

    b= a[::]
    
    print(b)


####切片 逆序输出==reverse

    c = a[::-1]  
    print(c)

####截取元素前一百  不会出现下标越界
    d = a[:100]
    
    print(d)
    
    assert 0


####将list的偶数位上的数字替换为0

    a = [1,2,3,4,5,6]
    
    a[::2]  = [0]*int(len(a)/2)

#####in:  
    a[::2] = [0]*int(len(a)/2)

#####out:  
    [0, 2, 0, 4, 0, 6]

####sorted函数操作

#####in:
    a = [[5, 9, 2, 7, 6, 8, 1, 10, 3, 4]]
    sorted(a)
#####out:
    a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

####len max sum

#####in：
    省略
####序列解包多个序列
###方法1（ZIP函数）:

#####in:
    keys = ['a','b','c','d']
    values = [1,2,3,4]
    for[k,v] in zip(keys,values):
        print((k,v),end='')
#####out:
    ('a', 1)('b', 2)('c', 3)('d', 4)          
        
###方法2(使用序列解包遍历enumerate对象)：
<h5>in:  

    x = ['a','b','c']
    for i,v in enumerate(x):
        print('the value on position {0} is {1}'.format(i,v))

<h5>out:

    the value on position 0 is a
    the value on position 1 is b
    the value on position 2 is c
    
    
<h4>列表推导式：

<h5>in:
    
    x for x in range(10)
    等价于
    l = []
    for x in range(10)
        l.append(x)


<h5>out:

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



<h4>列表推导式2：


<h5>in:
    
    [for x in range(10) if x%2==0]


<h5>out:
    
    
    [0, 2, 4, 6, 8]


<h4>列表推导式3：


<h5>in:
    
    l = []
    vec = [[1,2,3],[4,5,6],[7,8,9]]
    [num for elem in vec for num in elem]
    等价于
    for elem in vec:
        for num in elem:
            l.append(num)
    等价于遍历顶层序列之后对拿到的对象进行二次遍历
    
            
        
<h5>out:
    
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9]



<h2>匿名

###匿名函数
    
#####in:
        a.sort(key = lambda x :len(str(x)))
#####out：





<h2>元组


<h3>*属于不可变序列，用圆括号定义。  
使用tuple函数将其他序列转换为元组  
没有append 没有pop 没有 insert  
也没有remove  
速度要更快  
代码安全  
元组可以作为字典的key  
也可以作为集合的元素  
安全性很高*




<h2>集合 Set

<h3>*无序可变，使用一对大括号绑定，元素不可重复，每一个element唯一*  
集合中元素只能是不可变类型
不能包含字典，列表，集合



<h3>集合的操作


<h4>直接赋值
    
#####in:


    a = {3,5}
    a.add(7)

#####out:
    
    {3, 5, 7}
    

<h4>set方法将其他的对象转换为集合（会自动剔除重复元素）




<h4>pop方法 并且返回删除元素

#####in:


    a = {3,5,7}
    a.pop()

#####out:
    
    3
    

<h4>remove方法 删除指定元素

#####in:


    a = {3,5,7}
    a.remove(3)

#####out:
    
    {5, 7}
    
<h5>clear方法 清空集合


#####in:


    a = {3,5,7}
    a.clear()

#####out:
    
    set()
    
    


<h2>dict字典  
<key,value>


<h3>Adict = {'name':'dong',
              'sex':'male',
              'age':37}
              

<h4>得到键对应的值
        
        in:
        Adict['name']
        
        
        out:
        'dong'
<h4>如果不存在抛出异常  

        in:
        Adict['lee']
        
        out:
        ---------------------------------------------------------------------------
        KeyError                                  
        Traceback (most recent call last)
        <ipython-input-53-5af70300a21e> in <module>
        ----> 1 Adict['lee']
        
        KeyError: 'lee'
<h4>用get方法获取指定的键  

        in:
        print(Adict.get('address'))
        
        print(Adict.get('address','SDIBT'))
        
        out:
        None
        SDIBT

<h4>获取键，赋值，追加值
        
        in:
        Adict['score'] = Adict.get('score',[])
        Adict['score'].append(98)
        Adict['score'].append(99)
        out:
        {'name': 'dong', 'sex': 'male', 'age': 37, 'score': [98, 99]}
<h4>modify dict 
        
        in:
        Adict['age']=38
        Adict
        out:
        {'name': 'dong', 'sex': 'male', 'age': 38, 'score': [98, 99]}
        
        in:
        Adict['address'] = 'SDIBT'
        {'name': 'dong',
         'sex': 'male',
         'age': 38,
         'score': [98, 99],
         'address': 'SDIBT'}
<h4>用items()方法获得字典的键值对
<h4>用keys()方法获得字典的键
<h4>用values()方法获得字典的值
<h4>del dict element clear()  pop() popitem()


<h2>if判断语句
    
<h3>小实例
    
    
    in：
    month = input('month\n')
    if int(month)==0:
        print('Spring')
    elif int(month)==1:
        print('summer')
    elif int(month)==2:
        print('autumn')
    elif int(month)==3:
        print('winter')
    else:
        print('are you kiding me ?')
    
    out：
    month
    2
    autumn
    
    1
    summer
    
    3
    winter
    
    0
    spring
        
    
<h3>鸡兔同笼问题  
<h4>假设鸡兔共30只 腿90条 试问 鸡兔各多少只
<h5>求解过程:
        
        
        in:
        a = 30
        b = 90
        for i in range(1,a):
            y = a - i
            if 2 * i + 4 * y == b:
                print("鸡有" + str(i) + "只，兔有" + str(y) + "只。")
        out:
        鸡有15只，兔有15只。
    
                



---
---
---
---
Date：2019.06.18  
Author:Dawn  
Location:Jinan   
Wechat：llmllm_llm  
[新浪微博](https://weibo.com/u/5034954422)
 
![blockchain](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=702257389,1274025419&fm=27&gp=0.jpg "区块链")

        
        