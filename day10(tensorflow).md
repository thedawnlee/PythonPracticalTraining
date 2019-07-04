#day9(tensorflow初体验)

<h2>tensorflow测试

        #import tensorflow
        #tensoflow Test
        # hello = tf.constant("hello tensorflow")
        #
        # sess = tf.Session()
        #
        #
        # print(sess.run(hello))
<h2>一个线性回归小例子
        
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


<h3>placeholder初体验
        
        import tensorflow as tf
        #placeholer暂时存取变量  如果要从外部传入数据 那就需要用到tf.placeholder然后以sess.run(***,feed_dict={input：**})
        input1 = tf.placeholder(tf.float32)
        
        input2 = tf.placeholder(tf.float32)
        
        
        output = tf.multiply(input1,input2)
        
        with tf.Session() as sess:
            print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))


<h2>神经网络初体验
        
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


Date：2019.06.18  
Author:Dawn  
Location:Jinan   
Wechat：llmllm_llm  
[新浪微博](https://weibo.com/u/5034954422)
 
![blockchain](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=702257389,1274025419&fm=27&gp=0.jpg "区块链")

        
        