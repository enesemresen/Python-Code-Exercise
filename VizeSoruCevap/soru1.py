# Belirtilen örüntüyü ve kaç adet olduğunu bulunuz => 225 225
#                                                     237

import cv2
x = cv2.imread('elHarezmi.jpg')
y = cv2.cvtColor(x,cv2.COLOR_RGB2GRAY)
sayac = 0
for i in range(y.shape[0]):
    for j in range(y.shape[1]):
        if y[i,j]==225 and y[i,j+1]==225 and y[i+1,j]==237:
            sayac+=1
            print(sayac,"oruntu bulundu")

cv2.waitKey(0)