"""flower.jpg" resmi üzerinde 1 pixel genişliğinde
siyah yatay çizgiler oluşturan programı FOR döngüsü
ile gerçekleştiriniz (15P)"""

import cv2
x = cv2.imread('elHarezmi.jpg')
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        if(i%10==0):
            x[i,j,:]=0
cv2.imshow('YatayCizgi',x)
cv2.waitKey(0)
cv2.destroyAllWindows()