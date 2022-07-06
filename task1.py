import cv2
img = cv2.imread("/Users/natalieqoursha/Documents/images//img1.png", cv2.IMREAD_COLOR)


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("image",gray)
cv2.waitKey(0)
