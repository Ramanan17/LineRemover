import numpy as np
import cv2



img = cv2.imread('input.png', 0)


kernel = np.ones((6, 6), np.uint8)


img_dilation = cv2.dilate(img, kernel, iterations=2)

cv2.imshow('Input', img)

cv2.imshow('Dilation', img_dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()


