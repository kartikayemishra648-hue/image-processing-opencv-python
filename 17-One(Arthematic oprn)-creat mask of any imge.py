import cv2, numpy

# we just use an empty image for the purpose of this MCVE
img = cv2.imread("H:\\mask.jpg")   
width = len(img[0])
height = len(img)

empty_img = numpy.zeros((height, width, 3), numpy.uint8)

i = 0
r = 0
c = 0

for line in img:
    c = 0

    for pixel in line:
        blue = pixel[0]
        green = pixel[1]
        red = pixel[2]

        if green != max(red, green, blue) or green < 35:
            # this has a greenishy hue
            empty_img.itemset((r, c, 0), 255)

        c += 1
    r += 1
    
cv2.imshow("result",green)
cv2.waitKey(0)

cv2.destroyAllWindows()
    