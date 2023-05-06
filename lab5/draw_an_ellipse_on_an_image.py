import cv2
img = cv2.imread('Lenna_(test_image).png')
# cv2.ellipse(img, (250, 250), (150, 100), 0, 0, 360, (0, 255, 0), 3)
# cv2.imshow('circle', img)

# OR u can put the parameters into variables then pass those variables to the function
ellipse_center = (250, 250)
axes = (150, 100)
angle = 0
start_angle = 0
end_angle = 360
color = (0, 255, 0)
thickness = 3
cv2.ellipse(img, ellipse_center, axes, angle, start_angle, end_angle, color, thickness)
cv2.imshow('circle', img)
cv2.waitKey()
cv2.destroyAllWindows()
