# cv2.add(), cv2.addWeighted() etc.
import numpy as np
import cv2

#There is a difference between OpenCV addition and Numpy addition. 
#OpenCV addition is a saturated operation while Numpy addition is a modulo operation.

x = np.uint8([250])
y = np.uint8([10])
print("the open cv addtion==", cv2.add(x,y)) # 250+10 = 260 => 255
print("the numpy addtion==",x+y)          # 250+10 = 260 % 256 = 4

img1=cv2.imread("H:\\oprn.jpg")
img2=cv2.imread("H:\\a.jpg")


res1=cv2.add(img1,img2) #this is open cv addition of an image
cv2.imshow("result of open cv",res1)

res2=img1+img2 #this is numpy addition of an image
cv2.imshow("result of numpy",res2)

res3=cv2.subtract(img1,img2) #this is cv2 subtraction of an image1-img2
cv2.imshow("result of cv2 subtraction==",res3)

res4=cv2.subtract(img2,img1) #this is subtreaction of an image2-img1
cv2.imshow("result of cv2 subtraction from img2-img1==",res4)

cv2.waitKey(0)

cv2.destroyAllWindows()
