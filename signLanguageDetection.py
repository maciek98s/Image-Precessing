import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as image

#Read in Trump and convert to HSV
I = cv2.imread('C:/Users/corma/Desktop/New folder/Image Processing/GroupProject/Image-Processing-Project/DTemplate.png')
I2 = cv2.imread('C:/Users/corma/Desktop/New folder/Image Processing/GroupProject/Image-Processing-Project/formacsbitchass.png')
hsv = cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(I2,cv2.COLOR_BGR2HSV)

min_HSV = np.array([0, 48, 80], dtype = "uint8")
max_HSV = np.array([100, 155, 255], dtype = "uint8")

skinMask = cv2.inRange(hsv, min_HSV, max_HSV)
skinMask2 = cv2.inRange(hsv2, min_HSV, max_HSV)
shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

closing = cv2.morphologyEx(skinMask,cv2.MORPH_CLOSE,shape)
opening = cv2.morphologyEx(closing,cv2.MORPH_OPEN,shape)
closing2 = cv2.morphologyEx(skinMask2,cv2.MORPH_CLOSE,shape)
opening2 = cv2.morphologyEx(closing2,cv2.MORPH_OPEN,shape)
ROI = cv2.bitwise_and(I,I,mask=opening)
ROI2 = cv2.bitwise_and(I2,I2,mask=opening2)



cv2.imshow("Flesh", ROI)
cv2.imshow("Original", ROI2)
key = cv2.waitKey(0)

#Initilizing my Hull List
hull_list = []
hull_list2 = []
E = cv2.Canny(ROI, 30, 150)
E2 = cv2.Canny(ROI2, 30, 150)
#Used my canny to find contours
contours,_ =cv2.findContours(E, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
hull_list = sorted(contours, key=cv2.contourArea, reverse=True)
contours2,_ =cv2.findContours(E2, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
hull_list2 = sorted(contours2, key=cv2.contourArea, reverse=True)

img = cv2.drawContours(I, hull_list[0], -1, (0,0,255), 3)
img2 = cv2.drawContours(I2, hull_list2[0], -1, (0,0,255), 3)

ret = cv2.matchShapes(hull_list[0],hull_list2[0],1,0.0)
print(ret)

cv2.imshow("OrCormacinal", img)
cv2.imshow("Paul", img2)
key = cv2.waitKey(0)

if ret < 10:
    print("That is a C!")
else:
    print("lol dat aint no C")

#ret a = 10
#reb b = 33
#ret c = 4
#ret d = 55
#Ret C is the smallest therefore, more likely to me C