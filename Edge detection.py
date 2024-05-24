# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:02:45 2023

@author: sophi
"""

import cv2
from skimage.filters import sobel, prewitt, roberts,scharr

img = cv2.imread('D:/Python/python_for_image_processing_APEER-master/images/sandstone.tif',0)

sobel_img = sobel(img)
prewitt_img = prewitt(img)
roberts_img = roberts(img)
scharr_img = scharr(img)

cv2.imshow('Sobel',sobel_img)
cv2.imshow('Prewitt',prewitt_img)
cv2.imshow('Roberts',roberts_img)
cv2.imshow('Scharr', scharr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#######################################################################################

import cv2
import numpy as np

img = cv2.imread('D:/Python/python_for_image_processing_APEER-master/images/sandstone.tif',0)

edge_canny = cv2.Canny(img,50,80) #using 2 threshold

sigma = 0.3                       #auto canny
median = np.median(img)

lower = int(max(0,(1.0-sigma)*median)) #lower threshold is sigma %lower than median, if value is below 0 then tahe 0 as the median
upper = int(min(255,(1.0+sigma)*median)) #upper threshold is sigma % higher than median, if value is larger than 255 then take 255 as the median

auto_canny = cv2.Canny(img,lower,upper)

cv2.imshow('Canny detection', edge_canny)
cv2.imshow('Auto Canny detection', auto_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()







