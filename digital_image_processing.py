#Çerçeve
import cv2

elHarezmi = cv2.imread('elHarezmi.jpg')

elHarezmi[0:45, :, ] = 220
elHarezmi[0:45, :, 1] = 126
elHarezmi[0:45, :, 2] = 181

elHarezmi[:, 0:45] = [220, 126, 181]
elHarezmi[:, -45:0] = [220, 126, 181]
elHarezmi[-45:0, :] = [220, 126, 181]

#zebra
elHarezmi[:, 0::55] = 0
elHarezmi[0::55, :] = 0

#üzerindeki çizginin kalınlığı ayarlanabilir resim

i = 0
j = 30

for k in range(elHarezmi.shape[0]):
    for t in range(elHarezmi.shape[1]):
        elHarezmi[i:j, :] = 0
    i += 50
    j += 50


cv2.imshow('elHarezmi - Resmi', elHarezmi)

cv2.waitKey(0)



#bölme kullanrak gri yapmak
import cv2
import numpy as np

resim = cv2.imread('elHarezmi.jpg')

gri1 = (resim[:, :, 0] + resim[:, :, 1] + resim[:, :, 2]) / 3
gri2 = resim[:, :, 0] / 3 + resim[:, :, 1] / 3 + resim[:, :, 2] / 3

print(resim.dtype)
print(gri1.dtype)
print(gri2.dtype) #float tipinde gelir

                  
cv2.imshow('gri1', gri1)
cv2.imshow('gri2', gri2)
cv2.imshow('Orijinal', resim)

gri1Np = np.uint8(gri1) 
gri2Np = np.uint8(gri2) #int tipine dönüştürdük

print(resim.dtype)
print(gri1Np.dtype)
print(gri2Np.dtype)

cv2.imshow('gri1Np', gri1Np)
cv2.imshow('gri2Np', gri2Np)
cv2.imshow('Orijinal', resim)

cv2.waitKey(0)



#forsuz resim gri yapma
import cv2
import numpy as np

img = cv2.imread('elHarezmi.jpg')

#b * 0.11 + g * 0.44 + r * 0.28

img2gray = img[:, :, 0] * 0.11 + img[:, :, 1] * 0.44 + img[:, :, 2] * 0.28

img2gray = np.uint8(img2gray)

cv2.imshow('Orijinal', img)
cv2.imshow('Gri', img2gray)

cv2.waitKey(0)


#for ile resmi gri yapan abem
import cv2

image = cv2.imread('elHarezmi.jpg')

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i, j] = image[i, j, 0] * 0.11 + image[i, j, 1] * 0.44 + image[i, j, 2] * 0.28

cv2.imshow('Gri', image)
cv2.waitKey(0)



#resmi döndürme

import cv2
import numpy as np

abd = cv2.imread('elHarezmi.jpg')
mhm = abd[:, ::-1]
mhm = abd[::-1, :]
mhm = abd[::-1, ::-1]

cv2.imshow('Orijinal', abd)
cv2.imshow('Abd', mhm)
cv2.waitKey(0)
