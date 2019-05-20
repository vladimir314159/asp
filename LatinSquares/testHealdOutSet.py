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
from keras.models import load_model
import numpy as np
import os
import re
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

classifier = load_model('LS.h5')
print('foo')
trues = 0
falses = 0
for filename in os.listdir('./HealdOutSet/pictures'):
    num = re.match(r'LatinSquare([0-9]+)_n=([0-9]*)blocked=([0-9]+)\.lp\.png',str(filename)) #finds the value of n.
    print(num)
    if num is None:
        continue
    print("filename:\t"+filename)
    name = 'queen'+num.group(1)
    group = num.group(1)
    numBlocked = num.group(3)
    test_image = image.load_img('./HealdOutSet/pictures/'+filename, target_size = (64 , 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image / 255
    a = classifier.predict(test_image)
    a=a[0].tolist()
    print(a)
    a = list(a)
    print("index:",a.index(max(a)))
    if int(group) == a.index(max(a))+1:
        trues += 1
        print("true")
    else:
        falses +=1
        print("false")

print("true:",trues)
print("false:",falses)

