#for ile resmi gri yapma - make gray with for loop
import cv2

image = cv2.imread('elHarezmi.jpg')

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i, j] = image[i, j, 0] * 0.11 + image[i, j, 1] * 0.44 + image[i, j, 2] * 0.28

cv2.imshow('Gri', image)
cv2.waitKey(0)