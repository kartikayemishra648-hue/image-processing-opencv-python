import numpy as np
import cv2
img=cv2.imread("H:\\a.jpg")   #read image
#perform roi operation on image
#just replace pixels value

face = img[83:247,587:723]  #detect face from the image
img[83:247,441:577]=face#this area replaced by face
img[83:247,304:440]=face #the size of replace and selected area should be equal
img[83:247,588:724]=face
img[83:247,725:861]=face
cv2.imshow("img",img)   #Show
cv2.waitKey(0)
cv2.destroyAllWindows()



#164
#136

