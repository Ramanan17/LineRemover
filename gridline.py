import numpy as np
import cv2

#img = cv2.imread('input.png')

img = cv2.imread('input.png', 0)

# Taking a matrix of size 5 as the kernel
kernel = np.ones((6, 6), np.uint8)

# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
#img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=2)

cv2.imshow('Input', img)
#cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()


