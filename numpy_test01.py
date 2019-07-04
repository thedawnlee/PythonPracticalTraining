import numpy  as np
a = np.array([[1,2,3],[4,5,6]])


print(a)
print(a.shape)


a.shape = (3,2)
print(a)


print("=============================")
l = [1,2,3,4]

ll  = np.array(l)

print(ll)


ll.shape=(2,2)

print(ll)

print(ll[1, 1])

print(np.random.rand(5,5))

print("=============================")
#等差数组
print(np.linspace(0, 10, 11))

#对数数组

print(np.logspace(1, 10, 9, base=2))
print(np.logspace(0, 100, 10))

#全0的一维数组

print(np.zeros(
    (3, 3)
))

#全1的一位维数组

print(np.ones((3, 3)))


print("=================")


np.ones((1,3))

np.identity(3)

print(np.empty((3, 3)))
#信号处理 窗口函数
# np.hanning()
#
# np.blackman()
#
# np.kaiser()

#0,1中随机
print(np.random.rand(100, 100))

#标准的正态分布
print(np.random.standard_normal(2))

#对角线矩阵

print(np.diag([1, 2, 3]))

#追加元素

x = np.arange(8)

np.append(x,8)
print(x)

x = np.append(x,[9,10])

print(x)

x = np.insert(x,1,8)

print(x)


#repeat重复元素

#put 修改指定位置元素值
print("=============================")
a = np.array([1,2,3,4])
aa = np.array([10,20,30,40])

c = a*aa

print(c)


b = np.random.randint(1,10,(3,3),dtype=np.int)


print(c /a)