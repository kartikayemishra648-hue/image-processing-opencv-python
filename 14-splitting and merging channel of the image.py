import numpy as np
import cv2


img=cv2.imread("H:\\a.jpg")

img1 = cv2.split(img)
img2 = cv2.merge((img1))
cv2.imshow("aaaa",img2)
cv2.waitKey(0)

cv2.destroyAllWindows()