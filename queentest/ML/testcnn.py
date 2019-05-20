
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
from keras.models import load_model
import numpy as np
import cv2
np.set_printoptions(threshold=np.inf) #pint all of the array
classifier = load_model('epoch20number50.h5')
classifier0 = load_model('epoch25number20.h5')
classifier1 = load_model('epoch25number40.h5')
classifier2 = load_model('tanh.h5')
right = 0 
wrong = 0
for filename in os.listdir('./datasetI/test_set/queen4'):
    num = re.match(r'queen([0-9]+)[a-z0-9\.]*_n=([0-9]*)_([0-9]+)\.png',str(filename)) #finds the value of n.
    if num is None:
        continue
    print("filename:\t"+filename)
    name = 'queen'+num.group(1)
    n = num.group(2)
    numBlocked = num.group(3)
    test_image = image.load_img('./datasetI/test_set/queen4/'+filename, target_size = (64 , 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image / 255
    a = classifier0.predict(test_image)
    b = classifier.predict(test_image)
    c = classifier1.predict(test_image)
    d = classifier2.predict(test_image)
    print(a)
    print(b)
    print(c)
    print(d)
    if a+b+c+d >= .5:
        print("        \tqueen4")
        print("correct:\t",name)
        right += 1
    else:
        print("        \tqueen11")
        print("correct:\t",name)   
        wrong += 1 

print("sour creme\n")
for filename in os.listdir('./datasetI/test_set/queen11'):
    num = re.match(r'queen([0-9]+)[a-z0-9\.]*_n=([0-9]*)_([0-9]+)\.png',str(filename)) #finds the value of n.
    if num is None:
        continue
    print("filename:\t"+filename)
    name = 'queen'+num.group(1)
    n = num.group(2)
    numBlocked = num.group(3)
    test_image = image.load_img('./datasetI/test_set/queen11/'+filename, target_size = (64,64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image / 255
    a = classifier0.predict(test_image)
    b = classifier.predict(test_image)
    c = classifier1.predict(test_image)
    d = classifier2.predict(test_image)
    print(a)
    print(b)
    print(c)
    print(d)
    if a+b+c+d >= .5:
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
