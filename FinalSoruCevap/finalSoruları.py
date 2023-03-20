# Örüntü bulma
import cv2
image = cv2.imread('elHarezmi.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


x, y = gray.shape
counter = 0
for i in range(x):
    for j in range(y):
        if(gray[i, j] == 234 and gray[i, j + 1] == 235 and gray[i, j + 2] == 235 and gray[i + 1, j + 1] == 233):
            counter += 1
            print("{0}. örüntü bulundu. Koordinatları {1} {2}".format(counter, i, j))
            print(gray[i, j])
        

cv2.imshow('gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

###################################################################

#Video Oynat
import cv2
deneme = cv2.VideoCapture("CemalSüreyya.mp4")

ret, frame = deneme.read()

while True:
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

deneme.release()
cv2.destroyAllWindows()

###################################################################

#Bitwise_not
import cv2
from matplotlib import pyplot as plt

resim = cv2.imread('elHarezmi.jpg')

bitwiseDeneme = cv2.bitwise_not(resim)

plt.subplot(121), plt.imshow(resim), plt.title('Orijinal')
plt.subplot(122), plt.imshow(bitwiseDeneme), plt.title('bitwise_not')

cv2.waitKey(0)

###################################################################
# Siyah olan piksellerin rengini değiştiriniz
import cv2
from matplotlib import pyplot as plt
elHarezmi = cv2.imread('elHarezmi.jpg')

a,b,c = elHarezmi.shape

for i in range(a):
    for j in range(b):
        if(elHarezmi[i, j, :] == 0):
            elHarezmi[i, j] = [0, 0, 255]
            
            
# plt.subplot(121), plt.imshow(elHarezmi), plt.title('Orijinal')
cv2.imshow(elHarezmi)
cv2.waitKey(0)
