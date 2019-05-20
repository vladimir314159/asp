# Convolutional Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
# I did not write this code only edited form github.
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import Dropout
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import LSTM
from keras.layers import Dense
from keras.utils import plot_model
from keras.optimizers import Adam
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

import numpy as np
import cv2
# Initialising the CNN
lr = 0.1
look_back =1
Adam(lr=lr, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.01)
classifier = Sequential()
#classifier.add(LSTM(units=4, input_shape=(64, 64, 3 )))
# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
dropout = 0.2
# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Dropout(rate=dropout))
# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'tanh'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Dropout(rate=dropout))
classifier.add(Conv2D(32, (3, 3), activation = 'tanh'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 3, activation = 'relu'))
#classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0,  
                                   zoom_range = 0,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('HardInstances/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('HardInstances/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'categorical')
epoch_number = 500
epochs = 3
steps_validation = 145
history = classifier.fit_generator(training_set,
                         steps_per_epoch = epoch_number,
                         epochs = epochs,
                         validation_data = test_set,
validation_steps = steps_validation)  #should be 284

classifier.save('LS_hard.h5')
#print(history.history)
# Plot training & validation accuracy values
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
image_name = "Accuracy_dropHard"+str(dropout)+"_stepsPerEpoch"+str(epoch_number)+"numbEpochs"+str(epochs)+"lr"+str(lr)+".png"
plt.savefig(image_name)
plt.clf()
plt.cla()
plt.close()
# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
image_name = "Loss_dropHard"+str(dropout)+"_stepsPerEpoch"+str(epoch_number)+"numbEpochs"+str(epochs)+"lr"+str(lr)+".png"
plt.savefig(image_name)
plot_model(classifier, to_file='model.png')
#print(classifier.predict(test_set))