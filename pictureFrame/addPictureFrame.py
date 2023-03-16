#Çerçeve - Add picture frame
import cv2

elHarezmi = cv2.imread('elHarezmi.jpg')

elHarezmi[0:25, :, ] = 220
elHarezmi[0:25, :, 1] = 126
elHarezmi[0:25, :, 2] = 181

elHarezmi[:, 0:25] = [220, 126, 181]
elHarezmi[:, -25:] = [220, 126, 181]
elHarezmi[-25:, :] = [220, 126, 181]

cv2.imshow('elHarezmi - Resmi', elHarezmi)
cv2.waitKey(0)