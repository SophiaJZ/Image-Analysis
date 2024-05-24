# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:56:04 2023
GLOB AND CONVERT RGB COLOR
@author: sophi
"""

import cv2
import glob

path = 'D:/Python/python_for_image_processing_APEER-master/images/*.*'

img_num = 1

for file in glob.glob(path):
    print(file)
    a = cv2.imread(file)
    
    convert = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imwrite('D:/Python/ML/Convert_images+ str(img_num)+.jpg', convert)
    img_num +=1
    cv2.imshow('Color image',convert)
    
cv2.waitKey(0)
cv2.destroyAllWindows()    


#####################################################

import os

path = 'D:/Python/python_for_microscopists-master/python_for_microscopists-master/images/cell_images/test/Parasitized'

print(os.listdir(path))

for file in os.listdir(path):
    print(file)
    
os.imshow(file)