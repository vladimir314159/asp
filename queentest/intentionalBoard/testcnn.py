
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import Dropout
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.utils import plot_model
from keras.optimizers import Adam
from keras.preprocessing import *
from calculateBestEncoding import queen11, queen4
import os
import re
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from keras.models import load_model
import numpy as np
import cv2
np.set_printoptions(threshold=np.inf) #pint all of the array
classifier = load_model('dropout.5.h5')
right = 0 
wrong = 0
for filename in os.listdir('./dataset/training_set/queen4'):
    num = re.match(r'queen([0-9]+)[a-z0-9\.]*_n=([0-9]*)_([0-9]+)\.png',str(filename)) #finds the value of n.
    if num is None:
        continue
    print("filename:\t"+filename)
    name = 'queen'+num.group(1)
    n = num.group(2)
    numBlocked = num.group(3)
    test_image = image.load_img('./dataset/training_set/queen4/'+filename, target_size = (64 , 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image / 255
    a = classifier.predict(test_image)
    print(a)
    if a >= .5:
        print("        \tqueen4")
        print("correct:\t",name)
        right += 1
    else:
        print("        \tqueen11")
        print("correct:\t",name)   
        wrong += 1 

print("sour creme\n")
for filename in os.listdir('./dataset/training_set/queen11'):
    num = re.match(r'queen([0-9]+)[a-z0-9\.]*_n=([0-9]*)_([0-9]+)\.png',str(filename)) #finds the value of n.
    if num is None:
        continue
    print("filename:\t"+filename)
    name = 'queen'+num.group(1)
    n = num.group(2)
    numBlocked = num.group(3)
    test_image = image.load_img('./dataset/training_set/queen11/'+filename, target_size = (64,64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image / 255
    b = classifier.predict(test_image)
    print(b)
    if b >= .5:
        print("        \tqueen4")
        print("correct:\t",name)
        wrong += 1
    else:
        print("        \tqueen11")
        print("correct:\t",name) 
        right += 1
print("correct:\t",right)
print("wrong:\t",wrong)
print("percent correct:\t",right/(right+wrong)*100)
"""
classifier.evaluate(test_set)
prob = classifier.predict_classes(test_set)
print(prob)
"""
