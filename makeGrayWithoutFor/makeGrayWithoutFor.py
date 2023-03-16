#forsuz resim gri yapma - make gray without for loop
import cv2
import numpy as np

img = cv2.imread('elHarezmi.jpg')

#b * 0.11 + g * 0.44 + r * 0.28

img2gray = img[:, :, 0] * 0.11 + img[:, :, 1] * 0.44 + img[:, :, 2] * 0.28

img2gray = np.uint8(img2gray)

cv2.imshow('Orijinal', img)
cv2.imshow('Gri', img2gray)

cv2.waitKey(0)