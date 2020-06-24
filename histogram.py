import cv2
import numpy as np
from matplotlib import pyplot as plt

# This is histogram for picture.

img = cv2.imread('a1.png')    # Choose your image
color = ('b','g','r')
for i,col in enumerate(color):
     histr = cv2.calcHist([img],[i],None,[256],[0,256])
     plt.plot(histr,color = col)
     plt.xlim([0,256])
plt.title("Histogram")
plt.show()
