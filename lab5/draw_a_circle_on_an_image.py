import cv2
img = cv2.imread('Lenna_(test_image).png')
cv2.circle(img, (255, 255), 70, (0, 255, 0), 3)
cv2.imshow('circle', img)
cv2.waitKey()
cv2.destroyAllWindows()
