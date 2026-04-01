import numpy as np
import cv2

#This is also image addition, but different weights are given to images ,
#so that it gives a feeling of blending or transparency

img1=cv2.imread("H:\\oprn.jpg") #take two images
img2=cv2.imread("H:\\a.jpg")

blnd= cv2.addWeighted(img1,0.7,img2,0.3,0) #image adddition usind open cv
#here zero use as gamma function in the image

cv2.imshow('Result',blnd)
cv2.waitKey(0)
cv2.destroyAllWindows()