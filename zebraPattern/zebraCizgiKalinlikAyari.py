# 3 for ile zebra deseni çizgi kalınlık ayarı

import cv2
elHarezmi = cv2.imread('elHarezmi.jpg')
a,b,c = elHarezmi.shape

for i in range(a):
    for j in range(0, b, 50):
        for k in range(20): # kalınlık ayarını max 49 olacak şekilde ayarlayabiliriz. 50 olursa resim tamamen siyah olur
            elHarezmi[i,j] = 0
            j = j + 1
        
cv2.imshow('elHarezmi - Resmi', elHarezmi)
cv2.waitKey(0)

############################################# 
# çizgi kalınlığı ayarlanabilir zebra deseni

import cv2
elHarezmi = cv2.imread('elHarezmi.jpg')

i = 0
j = 50

a,b,c = elHarezmi.shape

for k in range(a):
    for t in range(b):
        elHarezmi[: ,i:j] = 0
    i += 100
    j += 100


cv2.imshow('elHarezmi - Resmi', elHarezmi)
cv2.waitKey(0)