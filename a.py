import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
# 参数初始化
filename = r'ts.xls'
data = pd.read_excel(filename)
# 此处的 [:, : 8] 的意思是，切片所有的行和 1- 8列的数据  # 此处的 as_matrix 函数是
# 将数据框数据结构转换为使用数组的数据结构
x = data.iloc[:,:8].as_matrix()
# 此处的 [:, 8] 的意思是， 切片所有的行和第 9 列 ，
# 注：这里的数字实际上是第 n 列 - 1
y = data.iloc[:,8].as_matrix()
# 建立随机逻辑回归模型，筛选变量
#  可以使用参数设置阈值： selection_threshold = 0.5 等
rlr = RLR()
# 训练模型
rlr.fit(x, y)
# 获取特征筛选结果，也可以通过 .scoress_方法获取各个特征的分数
rlr.get_support()
# 通过.score方法获取各个特征的分数
data2=data.drop(u'违约',1)
print(u'特        征 ：%s' % '  '.join(data2.columns[:8]))
print(u'对应特征分数：%s' % rlr.scores_)
print(u'通过随机逻辑回归模型特征选择结束。')
print(u'有效特征为：%s' % ','.join(data2.columns[rlr.get_support()]))
# 筛选好的特征
x = data[data2.columns[rlr.get_support()]].as_matrix()
# 建立逻辑回归模型
lr = LR()
# 用筛选好的特征数据训练模型
lr.fit(x, y)
print(u'逻辑回归模型训练结束')
# 给出模型的平均正确率
print(u'模型的平均正确率为：%s' % lr.score(x, y))
