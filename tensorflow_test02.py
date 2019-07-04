import tensorflow as tf
#placeholer暂时存取变量  如果要从外部传入数据 那就需要用到tf.placeholder然后以sess.run(***,feed_dict={input：**})
input1 = tf.placeholder(tf.float32)

input2 = tf.placeholder(tf.float32)


output = tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))