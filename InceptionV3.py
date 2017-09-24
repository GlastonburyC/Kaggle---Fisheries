from keras.applications.inception_v3 import InceptionV3
import os
from keras.layers import Flatten, Dense, AveragePooling2D,MaxPooling2D
from keras.models import Model, load_model
from keras.optimizers import RMSprop, SGD, adam
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.models import load_model
import shutil
import random
import sys
import keras
import matplotlib
matplotlib.use('Agg');
import matplotlib.pyplot as plt
import os
from scipy import ndimage, misc
import scipy.misc
import re,glob
import cv2
from train_val_split import train_val_split

os.environ["CUDA_VISIBLE_DEVICES"] = '0'

root_train = ''
root_val = ''
root_total = ''

#classes = ['',''.....]

train_val_split(prop=0.8)

train_imgs = glob.glob('')

for filename in train_imgs:
    image = ndimage.imread(filename, mode="RGB")
    image_resized = misc.imresize(image, (299,299))
    out_file=filename.split('.')[0].split('/')[1]
    cv2.imwrite(filename,image_resized)

learning_rate = 0.0001
img_width = 299
img_height = 299
nbr_train_samples = ''
nbr_validation_samples = ''
nbr_epochs = 50
batch_size = 64
train_data_dir = ''
val_data_dir = ''

best_model_file = "best.weights.h5"
best_model = ModelCheckpoint(best_model_file, monitor='val_loss', verbose = 1, save_best_only = True)


print('Loading InceptionV3 Weights ...')
InceptionV3_notop = InceptionV3(include_top=False, weights='imagenet',
                    input_tensor=None, input_shape=(299, 299, 3))


print('Adding Average Pooling Layer and Softmax Output Layer ...')
output = InceptionV3_notop.get_layer(index = -1).output
output = MaxPooling2D((8, 8), strides=(8, 8), name='max_pool')(output)
output = Flatten(name='flatten')(output)
output = Dense(2, activation='softmax', name='predictions')(output)

InceptionV3_model = Model(InceptionV3_notop.input, output)

optimizer = SGD(lr = learning_rate, momentum = 0.9, nesterov = True)
InceptionV3_model.compile(loss='categorical_crossentropy', optimizer = optimizer, metrics = ['accuracy'])

es=EarlyStopping(monitor='val_loss', patience = 10,
                                  verbose = 1)

tbCallBack=keras.callbacks.TensorBoard(log_dir='Graph', histogram_freq=0,
          write_graph=True, write_images=True)


# create a generator which will produce augmented versions of training images.
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.3,
        rotation_range=180.,
        width_shift_range=0.3,
        height_shift_range=0.3,
        horizontal_flip=True)

train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size = (img_width, img_height),
        batch_size = batch_size,
        shuffle = True,
        classes = classes,
class_mode = 'categorical')


val_datagen = ImageDataGenerator(rescale=1./255)


# create a generator which will produce augmented versions of validation images.
validation_generator = val_datagen.flow_from_directory(
        val_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        shuffle = True,
        classes = classes,
        class_mode = 'categorical')

# fit the model and track the validation loss function
InceptionV3_model.fit_generator(
        train_generator,
        steps_per_epoch = round(nbr_train_samples/batch_size),
        nb_epoch = nbr_epochs,
        validation_data = validation_generator,
        validation_steps = round(nbr_validation_samples/batch_size),
        callbacks = [best_model,tbCallBack,es])
