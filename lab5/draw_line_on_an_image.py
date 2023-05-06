import cv2
img = cv2.imread('circles.jpg')
cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 3)
cv2.imshow('line', img)

# draw an arrowed line
cv2.arrowedLine(img, (0, 0), (255, 255), (0, 0, 255))
cv2.imshow('arrowed_line', img)
cv2.waitKey()
cv2.destroyAllWindows()
