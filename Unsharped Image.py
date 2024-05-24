# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:45:32 2023

@author: sophi
"""

from skimage import io
from skimage.filters import unsharp_mask

img = io.imread('D:/Python/python_for_microscopists-master/python_for_microscopists-master/images/MRI_images/BM3D_denoised.tif')
unsharpened_img = unsharp_mask(img,radius=10,amount=2)

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(12,12))
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Original Image')

ax2 = fig.add_subplot(1,2,2)
ax2.imshow(unsharpened_img, cmap='gray')
ax2.title.set_text('Unsharped Image')

plt.show()