# Resim üzerinde belirli örüntünün kaç adet olduğunu gösteren kod bloğu

import cv2

elHarezmi = cv2.imread('elHarezmi.jpg')
gray = cv2.cvtColor(elHarezmi, cv2.COLOR_BGR2GRAY)

a,b = gray.shape
sayac = 0
for i in range(a):
    for j in range(b):
        if(gray[i,j] == 97 and gray[i + 1, j] == 76):
            gray[i,j] = 0 
            gray[i + 1,j] = 0
            sayac += 1 
            print("Deneme:" + str(sayac))

cv2.imshow('gray', gray)
cv2.waitKey(0)

#############################################
# Resmi X ve Y eksenlerine göre simetrisini alan kod bloğu

import cv2
from matplotlib import pyplot as plt

elHarezmi = cv2.imread('elHarezmi.jpg')

elHarezmiY = elHarezmi[::,::-1]
elHarezmiX = elHarezmi[::-1, ::]
elHarezmiXY = elHarezmi[::-1, ::-1]

plt.subplot(221), plt.imshow(elHarezmi), plt.title("Orijinal")
plt.subplot(222), plt.imshow(elHarezmiY), plt.title("Y Eksene Göre Simetri")
plt.subplot(223), plt.imshow(elHarezmiX), plt.title("X Eksene Göre Simetri")
plt.subplot(224), plt.imshow(elHarezmiXY), plt.title("X-Y Eksene Göre Simetri")

cv2.waitKey(0)

# ################################################
# Resim üzerinde belirli renk aralığındaki pikselleri boyayan kod bloğu

import cv2
from matplotlib import pyplot as plt

orj = cv2.imread('elHarezmi.jpg')
elHarezmi = cv2.imread('elHarezmi.jpg')
a, b, c = elHarezmi.shape

for i in range(a):
    for j in range(b):
        if(elHarezmi[i, j, 0] >= 150 and elHarezmi[i, j, 1] >= 80 and elHarezmi[i, j, 2] >= 120):
            elHarezmi[i, j] = [125, 125, 125]
            
plt.subplot(121), plt.imshow(orj), plt.title('Orijinal')
plt.subplot(122), plt.imshow(elHarezmi), plt.title('Deneme')
cv2.imshow('elHarezmi', elHarezmi)

cv2.waitKey(0)


# ################################################# rgb(181,126,220)
# Belirli renk aralığındaki piksellerden kaç adet olduğunu yazan kod bloğu

import cv2
from matplotlib import pyplot as plt

elHarezmi = cv2.imread('elHarezmi.jpg')

a, b, c = elHarezmi.shape
kahverenk = 0
kahverenkDegil = 0
for i in range(a):
    for j in range(b):
        if(elHarezmi[i, j, 0] == 220 and elHarezmi[i, j, 1] == 126 and elHarezmi[i, j, 2] == 181):
            kahverenk = kahverenk + 1
            
        else:
            kahverenkDegil = kahverenkDegil + 1
            
if kahverenkDegil > kahverenk:
    print('kahverenk: ' + str(kahverenk))
    print('kahverenkDegil: ' + str(kahverenkDegil))
    
cv2.imshow('elHarezmi', elHarezmi)
cv2.waitKey(0)

# ###########################################
# Resim öteleme 

import cv2
from matplotlib import pyplot as plt

elHarezmi = cv2.imread('elHarezmi.jpg')
elHarezmiCopy = elHarezmi.copy()
elHarezmiCopy[:,:] = 0

a, b, c = elHarezmi.shape

for i in range(a - 50):
    for j in range(b - 50):
        elHarezmiCopy[i + 50, j + 50] = elHarezmi[i, j]
        
plt.subplot(121), plt.imshow(elHarezmi), plt.title('Orijinal')
plt.subplot(122), plt.imshow(elHarezmiCopy), plt.title('Ötelenme')
        

cv2.waitKey(0)

# ###########################################
# Resim öteleme 

import cv2
from matplotlib import pyplot as plt

elHarezmi = cv2.imread('elHarezmi.jpg')
plt.subplot(121), plt.imshow(elHarezmi), plt.title('Orijinal')
elHarezmiCopy = elHarezmi.copy()

elHarezmi[:,:] = 0
a, b, c = elHarezmi.shape

for i in range(a - 50):
    for j in range(b - 50):
        elHarezmi[i + 50, j + 50] = elHarezmi[i, j]
        

plt.subplot(122), plt.imshow(elHarezmiCopy), plt.title('Ötelenme')

cv2.waitKey(0)

# #########################################
