
import numpy as np
from matplotlib import pyplot as plt
import cv2
import math
import random

#This uses cv2.imread to read in an image and assign it to im1
im1 = cv2.imread('bearissad3.jpg')

#This uses cv2.cvtColor to convert from color to grayscale
img = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)

#creates the length and width dimensions of the numpy array
length, width = img.shape

#sets the radius of the circle created in the image
radius = 0.4*min(length,width)

#the for loops loop through the 2d array.
for i in range(length):
    for j in range(width):
        #To create negative image uncomment below! This reverses the pixel intensities.
        #img[i,j] = 255-img[i,j]
        #this formula produces the circle around the image
        if math.sqrt((i-length/2)**2 + (j-width/2)**2) > radius:
            #this randomizes the pixels outside of the circle which creates an effect on the outer part of the image.
            img[i, j] = random.random()*255

plt.figure()
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
