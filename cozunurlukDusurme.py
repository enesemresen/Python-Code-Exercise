# Çözünürlük düşürme
import cv2
from matplotlib import pyplot as plt

lavanta = cv2.imread('lavanta.jpg')
lavanta2 = lavanta[::2, ::2]

plt.subplot(121),plt.imshow(lavanta),plt.title("Lavanta")
plt.subplot(122),plt.imshow(lavanta2),plt.title("Lavanta2")

cv2.waitKey(0)