import cv2
img = cv2.imread('../route-fifty-lead-image.jpg')
# Average filter
# avg = cv2.blur(img, (5, 5))
# cv2.imshow('average', avg)

# Gaussian blur
# gaussian = cv2.GaussianBlur(img, (7, 7), 0)
# cv2.imshow('gaussian', gaussian)

# median blur
# median = cv2.medianBlur(img, 5)
# cv2.imshow('median', median)

# bilateral filter
# bilateral = cv2.bilateralFilter(img, 9, 75, 75)
# cv2.imshow('bilateral', bilateral)

cv2.imshow('originalImage', img)
cv2.waitKey()
cv2.destroyAllWindows()

