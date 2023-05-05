import cv2
import numpy as np
from scipy import ndimage as nd
img = cv2.imread('route-fifty-lead-image.jpg')

# Q1
gaussian = cv2.GaussianBlur(img, (7, 7), 0)
# cv2.imshow('gaussian', gaussian)

# Q2
canny = cv2.Canny(img, 200, 300)
# cv2.imshow('canny', canny)

# Q3
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
merged = cv2.add(sobel_x, sobel_y)
# cv2.imshow('sobel_x', sobel_x)
# cv2.imshow('sobel_y',sobel_y)
# cv2.imshow('merged', merged)

# Q4
sch_rr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
sch_rr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)
# cv2.imshow('sch_rr_x', sch_rr_x)
# cv2.imshow('sch_rr_y', sch_rr_y)

# Q5
laplacian = cv2.Laplacian(img, cv2.CV_64F)
# cv2.imshow('laplacian', laplacian)

# Q6
kernel_3x3 = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])
k3 = nd.convolve(img, kernel_3x3)
blurred = cv2.GaussianBlur(img, (17, 17), 0)
g_hpf = img-blurred
cv2.imshow('3x3', k3)

cv2.waitKey()
cv2.destroyAllWindows()
