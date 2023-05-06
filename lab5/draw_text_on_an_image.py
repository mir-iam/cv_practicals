import cv2
img = cv2.imread('Lenna_(test_image).png')
text = 'open Cv'
org = (150, 150)
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 2
color = (0, 255, 0)
thickness = 3
cv2.putText(img, text, org, fontFace, fontScale, color, thickness)
cv2.imshow('text', img)
cv2.waitKey()
cv2.destroyAllWindows()
