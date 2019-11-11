import tensorflow as tf

((train_data, train_labels),(test_data, test_labels)) = tf.keras.datasets.fashion_mnist.load_data()

with open('data/train.txt', 'w') as output:
  for num, (image, label) in enumerate(zip(train_data, train_labels)):
    output.write('%d:%s:%d' % (num, ','.join(map(str, image.flatten().tolist())), label))
    output.write('\n')

with open('data/test.txt', 'w') as output:
  for num, (image, label) in enumerate(zip(test_data, test_labels)):
    output.write('%d:%s:%d' % (num, ','.join(map(str, image.flatten().tolist())), label))
    output.write('\n')