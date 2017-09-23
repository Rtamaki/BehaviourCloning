import csv
import os
import matplotlib.pyplot as mpplot
import matplotlib.image as mpimg
import numpy as np


lines = []
with open('./driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)


directory_path = os.path.dirname(os.path.abspath(__file__))

images = []
measurements = []

for line in lines:
    source_path = line[0]
    filename = source_path.split('/')[-1]
    current_path = directory_path + "/IMG/" + filename
    image = mpimg.imread(current_path)
    measurement = line[3]
    images.append(image)
    flipped_image = np.fliplr(image)
    images.append(flipped_image)
    measurements.append(measurement)
    measurement_flipped = -float(measurement)
    measurements.append(str(measurement_flipped))

X_train = np.array(images)
y_train = np.array(measurements)

from keras.models import Sequential, Model
from keras.layers import Flatten, Dense, Lambda, Convolution2D, MaxPooling2D, Cropping2D, Dropout, Conv2D


model = Sequential()
model.add(Cropping2D(cropping=((50,20), (0,0)), input_shape=(160, 320, 3)))
model.add(Lambda(lambda x: (x/255.0) - 0.5))
model.add(Conv2D(64, (5, 5), activation='relu', subsample=(2, 2)))
model.add(MaxPooling2D())
model.add(Dropout(0.5))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(200))
model.add(Dropout(0.5))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))






model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.1, shuffle=True, epochs=2, batch_size=32)
print("Finished training. Now saving model")
model.save('model.h5')