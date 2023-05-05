# convert from BGR to GRAY
import cv2
import matplotlib.pyplot as plt
# originalImage = cv2.imread('smdtownhall.jpg')
# grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
# cv2.imshow('colored', originalImage)
# cv2.imshow('gray', grayImage)
# cv2.waitKey()
# cv2.destroyAllWindows()

# originalImage = cv2.imread('route-fifty-lead-image.jpg')
# grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
# (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow('gray', grayImage)
# cv2.imshow('BW', blackAndWhiteImage)


# convert from BGR to RGB

# BGRImage = cv2.imread('route-fifty-lead-image.jpg')
# RGBImage = cv2.cvtColor(BGRImage, cv2.COLOR_BGR2RGB)
# cv2.imshow('BGR', BGRImage)
# cv2.imshow('RGB', RGBImage)
# cv2.waitKey()
# cv2.destroyAllWindows()


# split the image to three channels

# originalImage = cv2.imread('golde.jpg')
# B, G, R = cv2.split(originalImage)
# m = cv2.merge((B, G, R))
# cv2.imshow('Blue channel', B)
# cv2.imshow('Green channel', G)
# cv2.imshow('Red channel', R)
# cv2.imshow('merged', m)
# cv2.waitKey()
# cv2.destroyAllWindows()
# plt.show()

# convert from BGR to HSV

# originalImage = cv2.imread('golde.jpg')
# HSVImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)
# cv2.imshow('original', originalImage)
# cv2.imshow('HSV', HSVImage)
# H = HSVImage[:, :, 0]
# S = HSVImage[:, :, 1]
# V = HSVImage[:, :, 2]
# cv2.imshow('hue', H)
# cv2.imshow('saturation', S)
# cv2.imshow('value', V)
# cv2.waitKey()
# cv2.destroyAllWindows()
# plt.show()

# originalImage = cv2.imread('golde.jpg')
# half = cv2.resize(originalImage, (0, 0), fx=0.5, fy=0.5)
# bigger = cv2.resize(originalImage, (1050, 1610))
# stretch_near = cv2.resize(originalImage, (780, 540), interpolation=cv2.INTER_NEAREST)
# cv2.imshow('original', originalImage)
# cv2.imshow('half', half)
# cv2.imshow('bigger', bigger)
# cv2.imshow('stretched', stretch_near)
# cv2.waitKey()
# cv2.destroyAllWindows()
# plt.show()








