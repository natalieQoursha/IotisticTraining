import cv2 as cv
import numpy as np

img2= cv.imread('img2.png')
img=cv.imread('img.png')
img3=cv.imread('img3.png')
test1=cv.imread('testing1.png')
test2=cv.imread('testing2.png')


kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img2,kernel,iterations = 1)
dilation = cv.dilate(img2,kernel,iterations = 1)
opening = cv.morphologyEx(img2, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img3, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(test1, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(test1, cv.MORPH_BLACKHAT, kernel)


verti = np.concatenate((test1, blackhat), axis=1)

cv.imshow("image",verti)
cv.waitKey(7000)
cv.destroyAllWindows()

