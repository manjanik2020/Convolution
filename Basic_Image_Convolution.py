# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:33:27 2020

@author: Arpit patel
This file takes an Image and take convolution with given kernel
The kernel has to be 3X3 matrix.
The Image is 3D color Image
"""

from PIL import Image
import numpy as np
from skimage import io

def apply_conv(img,kernel):
    img=np.pad(img, ((1,1),(1,1)), 'constant')
    img1= img.copy()
    imgg=img.copy()
    numOfRows = img.shape[0]#zeros padding adjusment
    numOfCols = img.shape[1]#zeros padding adjusment
    for x in range(1, numOfRows-1):
        for y in range(1, numOfCols-1):
            img3=np.sum(np.multiply(imgg[np.ix_([x-1,x,x+1],[y-1,y,y+1])], kernel))
            img1[x,y]=img3
###remove padding
    img1 =img1[1:img1.shape[0]-1,1:img1.shape[1]-1]
    return img1
            
            
imgFile='puppy.jpg'
img = Image.open(imgFile)
im1 = Image.Image.split(img)
 
###now convolution
kernel=[[-1,0,1],
        [-1,0,1],
        [-1,0,1]]

iimage1 = np.array(img)
for i in range(0, 3): 
    im2=im1[i]
    pix = np.array(im2)
    pix=pix.astype(np.float16)
    image = apply_conv(pix,kernel)#Apply Convolution
    iimage = (image - np.min(image))/np.ptp(image)#in range 0 to 1
    iimage = 255.0*iimage
    iimage1[:,:,i]=iimage.astype(np.uint8)

io.imsave('out.png', iimage1)
io.imshow(iimage1)