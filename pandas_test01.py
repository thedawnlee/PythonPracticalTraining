import numpy as np
import pandas as pd

x = pd.Series([1,3,5,np.nan])

print(x)


# print(pd.date_range(start='20130101', end='20131231', freq='H'))
dates = pd.date_range(start='20130101', end='20131231', freq='M')
# print(pd.date_range(start='20130101', end='20191231', freq='Y'))


print(pd.DataFrame(np.random.randn(12, 4), index=dates, columns=list("ABCD")))

print(pd.DataFrame([np.random.randint(1, 100, 4) for i in range(12)], index=dates, columns=list("ABCD")))

print([np.random.randint(1, 100, 4) for i in range(12)])

#字典转换为DateFrame格式

# print(pd.DataFrame({'A': np.random.randint(1, 100, 4),
#                     'B': pd.date_range(start='20130101', periods=4, freq='D'),
#                     'C': pd.Series([1, 2, 3, 4], index=list(range(4)), dtype='float32'),
#                     'D': np.array([3] * 4, dtype='int32'),
#                     'E': pd.Categorical(["test", "train", "test", "train"]),
#                     "F": "foo"
#                     }))
df = pd.DataFrame({'A': np.random.randint(1, 100, 4),
                    'B': pd.date_range(start='20130101', periods=4, freq='D'),
                    'C': pd.Series([1, 2, 3, 4], index=['zhang','li','zhou','wang'], dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    "F": "foo"
                    })
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

#describe 获取数值，平均值 标准差 最大值 最小值

print(df.describe())


#二维数据的转置

print(df.T)

#排序
#axis = 0 代表纵向索引
#axis = 1 代表横向索引

df.sort_index(axis=0,ascending=False)
df.sort_index(axis=0,ascending=True)

#按值索引
df.sort_values(by="A")

#随机排序

sampler = np.random.permutation(len(df.index))
print(sampler)
print(df.take(sampler))
print("============================================")

#数据选择
print(df["A"])

print(69 in df['A'])

print(64 in df['A'].values)

#选择行列  第一个为行 第二个为列

print(df[0:2])


#选择多列
#用作索引

# print(df.loc[0:2, ['A', "C"]])

#定位 查询指定行列的数据值

print(df.at['zhang', 'A'])

#以数值的方式来获取数据
#用作下标
print("======================================")
print(df.iloc[3])


#查询第0行第一列位置的数据值
print(df.iloc[0, 1])
#查询第二行第二列位置的数据值
print(df.iloc[2, 2])
#按照给定条件进行查询
print(df[df.A > 50])
#按照给定条件进行查询
print(df[df["E"] == "test"])

print(df[df["A"].isin([51, 33])])