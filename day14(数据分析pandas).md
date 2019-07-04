#pandas
        
         pands：便捷的处理结构化数据


##数据分析模块
    
        
<h4>date_range函数：参数类型1.start  
                        2.end  
                        3.freq:1):H  
                               2):M  
                               3):Y  
                        
        in：
            pd.date_range(start='20130101', end='20131231', freq='M')
        out:
            DatetimeIndex(['2013-01-31', '2013-02-28', '2013-03-31', '2013-04-30',
            '2013-05-31', '2013-06-30', '2013-07-31', '2013-08-31',
            '2013-09-30', '2013-10-31', '2013-11-30', '2013-12-31'],
            dtype='datetime64[ns]', freq='M')
###pd,period生成日期间隔

        in:
            pd.period(start = "20130601",end = "20130630",freq = "W")

###DateFrame数据框
        
        生成DateFrame对象
        将日期类型转换为DateFrame对象
        in:
        dates = pd.date_range(start='20130101', end='20131231', freq='M')
        pd.DataFrame(np.random.randn(12, 4), index=dates, columns=list("ABCD"))   
        out:
                           A         B         C         D
        2013-01-31  0.160376  0.053405 -0.786390  0.196740
        2013-02-28  1.448855 -0.348209  0.101209  0.041661
        2013-03-31 -0.317766 -0.104251 -0.146258  0.334221
        2013-04-30 -1.512055  0.283944 -0.137704 -1.170040
        2013-05-31 -1.224679 -1.811670 -0.141750 -0.051531
        2013-06-30  0.974628 -0.135989 -0.094186  0.988703
        2013-07-31 -0.213751 -0.423694 -1.331667  0.575283
        2013-08-31  0.035131 -0.228200  0.513270  1.424074
        2013-09-30  2.454892  1.717468 -0.301250 -1.798910
        2013-10-31 -0.945194 -0.521914  1.334622 -0.828824
        2013-11-30  0.498964  1.385641 -0.346309  0.104953
        2013-12-31  0.704203  0.688478 -0.142807 -1.912619   
####字典类型转换为DateFrame类型
        
        in：
        pd.DataFrame({'A': np.random.randint(1, 100, 4),
                    'B': pd.date_range(start='20130101', periods=4, freq='D'),
                    'C': pd.Series([1, 2, 3, 4], index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    "F": "foo"
                    })
         out:
             A          B    C  D      E    F
            0  54 2013-01-01  1.0  3   test  foo
            1  96 2013-01-02  2.0  3  train  foo
            2  61 2013-01-03  3.0  3   test  foo
            3  92 2013-01-04  4.0  3  train  foo
####列表推导式转换为DateFrame类型
            
         in：
         print(pd.DataFrame([np.random.randint(1, 100, 4) for i in range(12)], index=dates, columns=list("ABCD")))
         out：
                      A   B   C   D
            2013-01-31  21  80  72  97
            2013-02-28  37  56  37   3
            2013-03-31  59  71  87   8
            2013-04-30  67  10   9  76
            2013-05-31  37  56  32  97
            2013-06-30  93  82  12  30
            2013-07-31  36  26  40  66
            2013-08-31  70  20  33  15
            2013-09-30  90  67  67   6
            2013-10-31  17  16  89  25
            2013-11-30  38  12   1  38
            2013-12-31  33  95  48  77      
####正态分布数值转换为DateFrame对象
        in：
        pd.DataFrame(np.random.randn(12, 4), index=dates, columns=list("ABCD"))
        out:
        
                           A         B         C         D
        2013-01-31  0.725492  0.060870 -0.565118 -0.290924
        2013-02-28  0.772514  1.392944  0.445835 -1.373000
        2013-03-31 -0.931468  0.564025  2.140997 -1.523830
        2013-04-30 -0.726556 -1.139239  0.204183 -0.139687
        2013-05-31  1.080767 -0.136377 -0.317529  0.406063
        2013-06-30 -1.203011  0.558248  0.111876  1.653814
        2013-07-31 -0.742677  1.042254  1.426628 -0.216841
        2013-08-31 -0.574281  0.285235 -0.580500  0.494710
        2013-09-30 -0.542297 -0.181619  1.007459  0.666526
        2013-10-31 -0.186051  0.302253  0.351677 -0.385840
        2013-11-30  0.583063  0.678709 -0.070067  1.324954
        2013-12-31 -1.478376  0.709314 -1.799320  1.851849
####二维数据的查看
        
        #二维数据的查看
        #默认显示前五行
        print(df.head())
        #前三行
        print(df.head(3))
        #显示索引
        print(df.index)
        #行数据
        print(df.columns)
        #值数据
        print(df.values)
        #最后两行
        df.tail(2)
####describe 获取数值，平均值 标准差 最大值 最小值
        
        df = pd.DataFrame({'A': np.random.randint(1, 100, 4),
                    'B': pd.date_range(start='20130101', periods=4, freq='D'),
                    'C': pd.Series([1, 2, 3, 4], index=['zhang','li','zhou','wang'], dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    "F": "foo"
                    })
         in:
         pd.describe()
         out:
                        A         C    D
            count   4.000000  4.000000  4.0
            mean   52.500000  2.500000  3.0
            std    33.110925  1.290994  0.0
            min    20.000000  1.000000  3.0
            25%    26.000000  1.750000  3.0
            50%    53.500000  2.500000  3.0
            75%    80.000000  3.250000  3.0
            max    83.000000  4.000000  3.0
         
         
####排序

        #axis = 0 代表纵向索引
        #axis = 1 代表横向索引
        
        df.sort_index(axis=0,ascending=False)
        df.sort_index(axis=0,ascending=True)
        
        #按值索引
        df.sort_values(by="A")
####随机排序
    
    in:
    sampler = np.random.permutation(len(df.index))
    print(sampler)
    print(df.take(sampler))
    out:
    [3 2 1 0]
        A          B    C  D      E    F
    wang   40 2013-01-04  4.0  3  train  foo
    zhou   22 2013-01-03  3.0  3   test  foo
    li     28 2013-01-02  2.0  3  train  foo
    zhang  68 2013-01-01  1.0  3   test  foo


####数据选择
        
##scipy
    
    scipy是基于numpy的科学计算核心包，它能与NumPy数组一起工作，并提供了许多用户友好和高效的数字实践，如实现插值，积分，优化，图像处理等等。
    
###中值滤波
    
    import random
    import numpy as np
    import scipy.signal as signal
    
    #一维中值滤波
    x = np.arange(0,100,10)
    random.shuffle(x)
    print(x)
    
    print(signal.medfilt(x, 3))
    #二维中值滤波
    #2d方式中值滤波
    #这种方式只支持int8 float32 float64









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

        
        
