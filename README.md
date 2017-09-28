# Behaviorial Cloning Project

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

Overview
---
This directory contains all the files for the behavior cloning project of Udacity Self Driving Cars.
Here I explain very briefly the architecture of the neural network and, more importantly, how I sampled during training mode for the model to behave correctly.


The Project
---
The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior 
* Design, train and validate a model that predicts a steering angle from image data
* Use the model to drive the vehicle autonomously around the first track in the simulator. The vehicle should remain on the road for an entire loop around the track.
* Summarize the results with a written report

### Dependencies
This lab requires:

* [CarND Term1 Starter Kit](https://github.com/udacity/CarND-Term1-Starter-Kit)

The lab enviroment can be created with CarND Term1 Starter Kit. Click [here](https://github.com/udacity/CarND-Term1-Starter-Kit/blob/master/README.md) for the details.

The following resources can be found in this github repository:
* drive.py
* video.py
* writeup_template.md

The simulator can be downloaded from the classroom. In the classroom, we have also provided sample data that you can optionally use to help train your model.

## Details About Files In This Directory

### The Neural Network

The architecture of the neural networks is similar to LeNet:

|Order | Layer Type | Number of Neurons/Rate | Filter Shape | 
| :---: |  :---: |  :---: |  :---: | 
|1 | Cropping | - | - |
|2 | Lamba(Normalization) | - | - |
|3 | 2D Convolution | 64 | (5,5) |
|4 | Max Pooling | - | - |
|5 | Dropout | 0.5 | - |
|6| 2D Convolution | 128 | (5,5) |
|7 | Max Pooling |- | - |
|8 | 2D Convolution | 256 | (5,5) |
|9 | Max Pooling |- | - |
|10 | Flatten | - | - |
|11 | Fully Connected| 200 | - |
|12 | Dropout | 0.5 | - |
|13 | Fully Connected| 100 | - |
|14 | Fully Connected| 50 | - |
|15 | Fully Connected| 10 | - |
|16 | Fully Connected| 1 | - |

For the training and validation process, I used Adam Optimizer to update the learning rate and 2 dropout layers to avoid overfitting. As there is 2 dropout layers I used more neurons than LeNet to also avoid underfitting.


### Training Examples

[image1]: ./LeavingLane.jpg "Leaving Lane"
[image2]: ./LeavingLane2.jpg "Other Leaving Lane"
[image3]: ./Specific_Contrats.jpg "Specific Lane Delimitations"

The most critical part, however, was selecting appropriate training data. At first, I only drove as I normaly would, most of the times I was at the center of the lane and the steering angle didn't change quickly nor was ever to great. Howerver, this procedure was proven wrong, since no data was sampled for critical situations, additionaly, the steering angle never was big even when obviously necessary (the car would leave the lane).
After noticing this, I changed my approach. Instead of focusing on how to drive as I normally would, I sampled situations where the car would live the lane if no strong action is taken. For the same neural network, the autonomous driving worked much better and completed the whole circuit. 
In the video.mp4  it becomes very clear that the behaviour isn't ideal, since the car lightly oscilates right and left inside the lane.

![Manualy creating situations on which the neural network will train][image1] 
![Other example on which the neural network will train][image2] 
![Manualy increasing the amount of data for less frequent lane delimitations][image3] 

In addition, the different types of lane delimitations apper with different frequencies in the circuit, which demands manually creating more training examples for more rare delimitations. A very clear example is the curve in the curve "pit stop" area, becase that is the only occasion where it appears, and for a very short distance. 

Furtheremore, I augmented the data by creating mirrored images from the original dataset. This process brings 2 advantages:
1) More training examples -> better accuracy and less overfitting
2) Avoid the NN to always add a positive(or negative) value to the steering angle, since during the whole circuit we are always slightly turning left. By using split images, the average of the steering angle is zero.


Another important observation is the fact that validation/training accuracy doesn't directly correspond to driving quality. This may not be obvious at first, but makes sense since they aren't the same measures. Additionaly, there aren't many samples and for the same cenario there may be different behaviours, since the samples were artificially created by a human.





