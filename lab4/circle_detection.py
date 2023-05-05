import cv2
import numpy as np

planets = cv2.imread('circles.jpg')
gray = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 120, param1=100, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(planets, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(planets, (i[0], i[1]), 2, (0, 0, 255), 3)
cv2.imshow('image', planets)
cv2.imshow('HoughCircles', planets)
cv2.waitKey()
cv2.destroyAllWindows()

