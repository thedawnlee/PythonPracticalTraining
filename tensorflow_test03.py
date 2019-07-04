import tensorflow as tf
import numpy as np

#搭建一个神经网络
#定义节点来接收数据
#定义神经层  定义隐藏层 定义预测层
#隐藏层
#添加一个隐藏层
#激活函数是把线性问题转换为非线性问题
def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size])+0.1)
    Wx_plus_b = tf.matmul(inputs,Weights)+biases
    if activation_function is None:
        outpus = Wx_plus_b
    else:
        outpus = activation_function(Wx_plus_b)
    return outpus


x_data = np.linspace(-1,1,300)[:,np.newaxis]
noise = np.random.normal(0,0.5,x_data.shape)

y_data = np.square(x_data)-0.5+noise

xs = tf.placeholder(tf.float32,[None,1])

ys = tf.placeholder(tf.float32,[None,1])

#输入值是xs，再隐藏层有10个神经元

ll = add_layer(xs,1,10,activation_function=tf.nn.relu)

prediction = add_layer(ll,10,1,activation_function=None)
#定义loss表达式

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()


sess.run(init)

for i in range(1001):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i%50==0:
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
