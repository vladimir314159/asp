


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
classifier= load_model('tanh.h5')
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
    test_image = test_image/255
    #print(test_image)
    binary = classifier.predict(test_image)
    foo = classifier.predict_classes(test_image)
    #generator = classifier.predict_generator(test_image)
    prob = classifier.predict_proba(test_image)
    #print(test_image)
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