# 矩阵
import tensorflow as tf
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

random_float = tf.random.uniform(shape=())

x = tf.constant([[1., 2.], [3., 4.]])
y = tf.constant([[5., 6.], [7., 8.]])

a = tf.add(x, y)
b = tf.matmul(x, y)

print(a, b)
