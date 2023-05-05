import numpy as np
import cv2
from scipy import ndimage

img = cv2.imread('../route-fifty-lead-image.jpg')
# smooth filter
kernel1 = np .array([[0.04, 0.04, 0.04, 0.04],
                     [0.04, 0.04, 0.04, 0.04],
                     [0.04, 0.04, 0.04, 0.04],
                     [0.04, 0.04, 0.04, 0.04],
                     [0.04, 0.04, 0.04, 0.04]])
# sharp filter
kernel2 = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])
smooth = cv2.filter2D(img, -1, kernel1)
sharp = cv2.filter2D(img, kernel2)
cv2.imshow('original', img)
cv2.imshow('smooth', smooth)
cv2.imshow('sharp', sharp)
cv2.waitKey()
cv2.destroyAllWindows()
