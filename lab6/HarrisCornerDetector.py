import cv2
import numpy as np
img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
# then we do dilate the result
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
img[dst > 0.01*dst.max()] = [0, 0, 255]
cv2.imshow('dst', img)
cv2.waitKey()
cv2.destroyAllWindows()
