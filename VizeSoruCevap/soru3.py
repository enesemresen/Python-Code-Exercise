"""Aşağıdaki soldaki 'ari1.jpg' resminde olmayıp
'ari2.jpg' resminde olan nesneleri tespit edip
'farklar.jpg' resmi içerisinde orjinal yerlerinde
gösteren programı yazınız. (25 P)"""

import cv2
x = cv2.imread('elHarezmi.jpg')
y = cv2.imread('elHarezmiFark.jpg')
fark = y-x
cv2.imshow('Farklar',fark)
cv2.waitKey(0)
cv2.destroyAllWindows() 