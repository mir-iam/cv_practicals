import cv2
import numpy as np

img = cv2.imread('sDQLM.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 120)
lines = cv2.HoughLinesP(edges, 1, np.pi/180.0, 20, minLineLength=20, maxLineGap=5)
for x1, x2, y1, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('edges', edges)
cv2.imshow('lines', img)
cv2.waitKey()
cv2.destroyAllWindows()
