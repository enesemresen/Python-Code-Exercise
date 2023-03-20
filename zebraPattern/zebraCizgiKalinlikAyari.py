# 3 for ile zebra deseni çizgi kalınlık ayarı

import cv2
lavanta = cv2.imread('lavanta.jpg')
a,b,c = lavanta.shape

for i in range(a):
    for j in range(0, b, 50):
        for k in range(20): # kalınlık ayarını max 49 olacak şekilde ayarlayabiliriz. 50 olursa resim tamamen siyah olur
            lavanta[i,j] = 0
            j = j + 1
        
cv2.imshow('Lavanta - Resmi', lavanta)
cv2.waitKey(0)

############################################# 
# çizgi kalınlığı ayarlanabilir zebra deseni

import cv2
lavanta = cv2.imread('lavanta.jpg')

i = 0
j = 50

a,b,c = lavanta.shape

for k in range(a):
    for t in range(b):
        lavanta[: ,i:j] = 0
    i += 100
    j += 100


cv2.imshow('Lavanta - Resmi', lavanta)
cv2.waitKey(0)