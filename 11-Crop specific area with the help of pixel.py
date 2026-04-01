import numpy as python
import cv2
img=cv2.imread("H:\\a.jpg") #read image
roi =img[79:250,576:716] #place starting and ending pixels
cv2.imshow("img",roi)   #Show
cv2.waitKey(0)
cv2.destroyAllWindows()
