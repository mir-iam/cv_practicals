import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../route-fifty-lead-image.jpg', cv2.IMREAD_GRAYSCALE)
(threshold, BW) = cv2.threshold(img, 220, 225, cv2.THRESH_BINARY)
kernel = np.ones((5, 5))

# dilation
# dilation = cv2.dilate(BW, kernel, iterations=2)
# cv2.imshow('erosion', dilation)

# erosion
# erosion = cv2.erode(BW, kernel, iterations=1)
# cv2.imshow('erosion', erosion)

# opening
# opening = cv2.morphologyEx(BW, cv2.MORPH_OPEN, kernel)
# cv2.imshow('opening', opening)

# closing
# closing = cv2.morphologyEx(BW, cv2.MORPH_CLOSE, kernel)
# cv2.imshow('closing', closing)

cv2.waitKey()
cv2.destroyAllWindows()
