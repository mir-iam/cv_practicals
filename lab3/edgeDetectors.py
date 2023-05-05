import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

img = cv2.imread('route-fifty-lead-image.jpg')
# Edge detection using custom kernel
# kernel_3x3 = np.array([[-1, -1, -1],
#                        [-1,  8, -1],
#                        [-1, -1, -1]])
#
# kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
#                        [-1,  1,  2,  1, -1],
#                        [-1,  2,  4,  2, -1],
#                        [-1,  1,  2,  1, -1],
#                        [-1, -1, -1, -1, -1]])
# k3 = ndimage.convolve(img, kernel_3x3)
# k5 = ndimage.convolve(img, kernel_5x5)
# blurred = cv2.GaussianBlur(img, (17, 17), 0)
# g_hpf = img-blurred
# cv2.imshow('3x3', k3)
# cv2.imshow('5x5', k5)
# cv2.imshow('g_hpf', blurred)

# edge detection using second derivative filters like laplacian and sobel, scharr derivatives
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobelImage = cv2.add(sobel_x, sobel_y)
# scharr operator
sch_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
sch_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)
# plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray'), plt.title('gray')
# plt.subplot(2, 3, 2), plt.imshow(img, cmap='gray'), plt.title('laplacian')
# plt.subplot(2, 3, 3), plt.imshow(img, cmap='gray'), plt.title('sobel_x')
# plt.subplot(2, 3, 4), plt.imshow(img, cmap='gray'), plt.title('sobel_y')
# plt.subplot(2, 3, 5), plt.imshow(img, cmap='gray'), plt.title('scharr_x')
# plt.subplot(2, 3, 6), plt.imshow(img, cmap='gray'), plt.title('scharr_y')
# plt.show()

# edge detection using Canny edge detector [ First derivative ] [linear]

canny = cv2.Canny(img, 200, 300)
cv2.imshow('canny', canny)
cv2.waitKey()
cv2.destroyAllWindows()


