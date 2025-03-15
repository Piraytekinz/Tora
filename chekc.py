#PERFORMING IMAGE PROCCESSING TECHNIQUES ON THE IMAGES FOR
#VALIDATION REASONS

import cv2 as cv

img = cv.imread('thunder-25689.png')

img = img[40:343, 90:805]

print(img.shape)

cv.imshow('img', img)

cv.imwrite('specto/thunder-25689.png', img)
cv.waitKey(0)