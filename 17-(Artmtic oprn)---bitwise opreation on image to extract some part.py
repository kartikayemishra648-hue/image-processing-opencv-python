import numpy as np
import cv2
    
#ou will see these functions : cv2.getTickCount, cv2.getTickFrequency etc.
t1 = cv2.getTickCount()   #for mesuring performance
# Load two images
img1 = cv2.imread("H:\\a.jpg")
img2 = cv2.imread("H:\\col.jpg")

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols ]
cv2.imshow("the position==0",roi)

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('mask--1',img2gray)          #cheak the mask
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('inverse mask--2',mask_inv)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('img1_bg--3 the and on img1',img1_bg)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow('img2-fg--4 the and on img2fg',img2_fg)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)

t2 = cv2.getTickCount()         #for measuring performance
time = (t2 - t1)/ cv2.getTickFrequency()   #diffrence to get actual time of execution
print("the total time is==",time)
cv2.waitKey(0)
cv2.destroyAllWindows()