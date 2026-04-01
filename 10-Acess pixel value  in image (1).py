#Let’s load a color image first:
import cv2
import numpy as np

image=cv2.imread("H:\\oprn.jpg")

#access a pixel value by its row and column coordinates.
#For BGR image, it returns an array of Blue, Green, Red values.
#For grayscale image, just corresponding intensity is returned.

px = image[100,100] #store cordibate in variable
print("the pixel of that co-ordinates==",px) #we get the pixel value


# accessing only blue pixel
blue = image[900,450,0]
print("the pixel having blue color==",blue)
red=image[950,450,0]
print("the all red pixels in image==",red)
print("the shape of image",image.shape)  #provide shape of image
print("the total number of pixel in image==",image.size) #give total number of pixl in image