import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

# draw the contours of an image
img = cv2.imread('openCV.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# print("Number of contours = "+str(len(contours)))
# cv2.drawContours(img, contours, -1, (255, 255, 0), 3)
# cv2.imshow('image', img)
# cv2.imshow('gray', gray)

# form a shape and then draw/highlight contours of that shape
img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
cv2.imshow('contours', color)
cv2.waitKey()
cv2.destroyAllWindows()
