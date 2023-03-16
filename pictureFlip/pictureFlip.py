#resmi döndürme - picture flip

import cv2
import numpy as np

abd = cv2.imread('elHarezmi.jpg')
mhm = abd[:, ::-1]
mhm = abd[::-1, :]
mhm = abd[::-1, ::-1]

cv2.imshow('Orijinal', abd)
cv2.imshow('Abd', mhm)
cv2.waitKey(0)
