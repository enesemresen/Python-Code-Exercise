#bölme kullanrak gri yapmak - make gray using partition
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