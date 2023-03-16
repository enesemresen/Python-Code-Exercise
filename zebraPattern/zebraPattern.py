#Zebra deseni - add zebra pattern to picture
import cv2

elHarezmi = cv2.imread('elHarezmi.jpg')

# elHarezmi[:, 0::55] = 0 # vertical lines
elHarezmi[0::55, :] = 0 # horizontal lines

cv2.imshow('elHarezmi - Resmi', elHarezmi)
cv2.waitKey(0)