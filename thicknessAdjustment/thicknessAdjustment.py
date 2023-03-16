#Üzerindeki çizginin kalınlığı ayarlanabilir resim - The thickness of the line on the picture can be adjusted
import cv2

elHarezmi = cv2.imread('elHarezmi.jpg')

i = 0
j = 30

for k in range(elHarezmi.shape[0]):
    for t in range(elHarezmi.shape[1]):
        elHarezmi[i:j, :] = 0
    i += 70
    j += 70

cv2.imshow('elHarezmi - Resmi', elHarezmi)
cv2.waitKey(0)