from __future__ import absolute_import, division, print_function

import matplotlib.pylab as plt

import tensorflow as tf
import tensorflow_hub as hub

import numpy as np
import PIL.Image as Image

from tensorflow.keras import layers

data_root = tf.keras.utils.get_file(
  'flower_photos','https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz',
   untar=True)
image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
image_data = image_generator.flow_from_directory(str(data_root))
for image_batch,label_batch in image_data:
  print("Image batch shape: ", image_batch.shape)
  print("Labe batch shape: ", label_batch.shape)
  break

classifier_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/classification/2" #@param {type:"string"}


def classifier(x):
    classifier_module = hub.Module(classifier_url)
    return classifier_module(x)


IMAGE_SIZE = hub.get_expected_image_size(hub.Module(classifier_url))

classifier_layer = layers.Lambda(classifier, input_shape = IMAGE_SIZE+[3])
classifier_model = tf.keras.Sequential([classifier_layer])
classifier_model.summary()

image_data = image_generator.flow_from_directory(str(data_root), target_size=IMAGE_SIZE)
for image_batch,label_batch in image_data:
  print("Image batch shape: ", image_batch.shape)
  print("Labe batch shape: ", label_batch.shape)
  break

grace_hopper = tf.keras.utils.get_file('image.jpg',
                                     'https://storage.googleapis.com/download.tensorflow.org/example_images/grace_hopper.jpg')
grace_hopper = Image.open(grace_hopper).resize(IMAGE_SIZE)
grace_hopper

grace_hopper = np.array(grace_hopper) / 255.0
grace_hopper.shape
result = classifier_model.predict(grace_hopper[np.newaxis, ...])
result.shape
predicted_class = np.argmax(result[0], axis=-1)
predicted_class
labels_path = tf.keras.utils.get_file('ImageNetLabels.txt',
                                    'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())
plt.imshow(grace_hopper)
plt.axis('off')
predicted_class_name = imagenet_labels[predicted_class]
_ = plt.title("Prediction: " + predicted_class_name)