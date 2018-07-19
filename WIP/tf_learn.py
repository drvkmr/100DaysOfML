import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

x = tf.placeholder(float, None)
y = x*2

with tf.Session() as session:
    data = [[1, 2, 3],
            [4, 5, 6]]
    result = session.run(y, feed_dict={x: data})
    print(result)
