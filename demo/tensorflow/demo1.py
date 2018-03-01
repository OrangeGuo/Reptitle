import os
# 关闭烦人的警告
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import tensorflow as tf 
import numpy as np 
# 创建一个计算图
sess=tf.Session()
# 生成数据
x_vals=np.random.normal(1,0.1,100)
y_vals=np.repeat(10.,100)
x_data=tf.placeholder(shape=[1],dtype=tf.float32)
y_target=tf.placeholder(shape=[1],dtype=tf.float32)
A=tf.Variable(tf.random_normal(shape=[1]))
my_output=tf.multiply(x_data,A)
loss=tf.square(my_output-y_target)
#init=tf.initialize_all_variables()
init=tf.global_variables_initializer()
sess.run(init)
print("A="+str(sess.run(A)))
my_opt=tf.train.GradientDescentOptimizer(learning_rate=0.02)
train_step=my_opt.minimize(loss)
for i in range(100):
    rand_index=np.random.choice(100)
    rand_x=[x_vals[rand_index]]
    rand_y=[y_vals[rand_index]]
    sess.run(train_step,feed_dict={x_data:rand_x,y_target:rand_y})
    if i%25==0:
        print("A="+str(sess.run(A)))
        print("Loss="+str(sess.run(loss,feed_dict={x_data:rand_x,y_target:rand_y})))
