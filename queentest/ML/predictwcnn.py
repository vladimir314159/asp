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
from keras.layers import Dense
from keras.utils import plot_model
from keras.optimizers import Adam
from calculateBestEncoding import queen11, queen4
import os
import re
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

import numpy as np
import cv2
# Initialising the CNN
lr = 0.2
Adam(lr=lr, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0001)
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
dropout = 0.1
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
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator
               
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0,  
                                   zoom_range = 0,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('datasetI/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('datasetI/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')
epoch_number = 30
epochs = 25
steps_validation = 100
history = classifier.fit_generator(training_set,
                         steps_per_epoch = epoch_number,
                         epochs = epochs,
                         validation_data = test_set,
validation_steps = steps_validation)  #could be up to 284
print(history)
#print(history.history)
# Plot training & validation accuracy values
classifier.save('tanh.h5')
'''
from keras.preprocessing import image

time_only_queen4 = []
time_classifier = []


i = 0 
for filename in os.listdir('./HealdOutSet'):
    print("filename:\t"+str(i)+filename)
    print(str(i))
    num = re.match(r'queen([0-9]+)[a-z0-9\.]*_n=([0-9]*)_([0-9]+)\.png',str(filename)) #finds the value of n.
    if num is None:
        continue
    name = 'queen'+num.group(1)
    n = num.group(2)
    numBlocked = num.group(3)
    filename1 = "./HealdOutSet/encodings/*.blocked_n="+str(n)+"_"+str(numBlocked)
    print("filename1:\t"+str(i)+filename1)
    cmd = "cp "+filename1+" ./HealdOutSet/encodings/blocked.lp "
    os.system(cmd)
    time4 = queen4(numBlocked,n,False)[0]
    print("time4:\t"+str(time4))
    time_only_queen4.append(time4)
    test_image = image.load_img('./HealdOutSet/'+filename, target_size = (64,64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    #print(test_image)
    binary = classifier.predict(test_image)
    foo = classifier.predict_classes(test_image)
    #generator = classifier.predict_generator(test_image)
    prob = classifier.predict_proba(test_image)
    print(test_image)
    #print("generator\t:",generator)
    print("prob\t:",prob)
    print("foo:\t",foo,"\n")
    if foo[0][0]<=0.5:
        time = queen11(numBlocked,n,False)[0]
    else:
        time = time4
    print("time_pre:\t"+str(time))
    time_classifier.append(time)
    i = i + 1
print(sum(time_classifier)/float(len(time_classifier)))
print(sum(time_only_queen4)/float(len(time_only_queen4)))
plt.plot(time_only_queen4)

plt.plot(time_classifier)
plt.title('predictions')
plt.ylabel('time')
plt.xlabel('instaince')

#plt.legend(['Train', 'Test'], loc='upper left')
image_name = "Predictions-cnn.png"
plt.savefig(image_name)
plt.clf()
plt.cla()
plt.close()
'''
'''
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
image_name = "Accuracy_drop"+str(dropout)+"_stepsPerEpoch"+str(epoch_number)+"numbEpochs"+str(epochs)+"lr"+str(lr)+".png"
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
image_name = "Loss_drop"+str(dropout)+"_stepsPerEpoch"+str(epoch_number)+"numbEpochs"+str(epochs)+"lr"+str(lr)+".png"
plt.savefig(image_name)
plot_model(classifier, to_file='model.png')
#print(classifier.predict(test_set))
'''
