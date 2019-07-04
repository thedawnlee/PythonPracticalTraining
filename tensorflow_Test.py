import tensorflow as tf
import numpy as np
#tensoflow Test
# hello = tf.constant("hello tensorflow")
#
# sess = tf.Session()
#
#
# print(sess.run(hello))

#create data to training
#创建数据
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3
print(x_data)
print(y_data)
#搭建模型
Weight = tf.Variable(tf.random_uniform([1],-1.0,1.0))

biases = tf.Variable(tf.zeros([1]))

y = Weight*x_data+biases

# print(y)

#计算误差

lose=tf.reduce_mean(tf.square(y-y_data))

#传播误差

optimizer = tf.train.GradientDescentOptimizer(0.5)

train = optimizer.minimize(lose)

#训练
#训练之前必须要对所有的variable

init = tf.global_variables_initializer()

#sess = tf.Session()
#使用python的上下文管理器来管理会话
with tf.Session() as sess:
    sess.run(init)

    for step in range(280):
       sess.run(train)
       if step%20 == 0:
           print(step,sess.run(Weight),sess.run(biases))


