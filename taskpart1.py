Last login: Wed Jul  6 22:20:50 on ttys000
(base) natalieqoursha@natalies-Air ~ % python3
Python 3.9.12 (main, Apr  5 2022, 01:53:17) 
[Clang 12.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> img = cv2.imread("/Users/natalieqoursha/Documents/images//img1.png", cv2.IMREAD_COLOR)
>>> 
>>> 
>>> gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
>>> cv2.imshow("image",gray)
>>> cv2.waitKey(0)











