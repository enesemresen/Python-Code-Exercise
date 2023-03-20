"""Aşağıdaki gösterimde orijinal 'ev.jpg' resmini sağdaki gibi
15 pixel öteleme işlemini gerçekleştirip
aynı pencerede yan yana gösteren programı yazınız. (25 P)
"""
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('lavanta.jpg')
yeni = cv2.imread('lavanta.jpg')

a,b,c = img1.shape

yeni[0:a,0:b] = 0

for i in range(a - 100): 
    for j in range(b-150):
        
        yeni[i + 100,j+150] = img1[i,j]
        
plt.subplot(2,2,1),plt.imshow(img1),plt.title('Orjinal')
plt.subplot(2,2,2),plt.imshow(yeni),plt.title('Oteleme')

