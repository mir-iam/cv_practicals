import cv2
img = cv2.imread('circles.jpg')
cv2.rectangle(img, (10, 10), (150, 150), (0, 0, 255))
cv2.imshow('circle', img)
cv2.waitKey()
cv2.destroyAllWindows()
