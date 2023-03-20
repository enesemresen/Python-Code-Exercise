"""Yandaki resim 200x200 boyutlarında RGB formatındadır.
Bu resmin kenarlarına resimde görüldüğü gibi 10 piksellik
yeşil bir çerçeve çizdiriniz. (10 P)"""

import cv2
x = cv2.imread('elHarezmi.jpg')
satir = x.shape[0]
sutun = x.shape[1]  
x[0:10,:,:] = [0,255,0]
x[:,0:10,:] = [0,255,0]
x[-10:,:,:] = [0,255,0]
x[:,-10:,:] = [0,255,0]

cv2.imshow('YesilCerceve',x)
cv2.waitKey(0)
cv2.destroyAllWindows()