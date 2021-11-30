#opencv-python
import cv2
import numpy as np

image = cv2.imread("image.jpg")

print(image)
print(image.shape)

b,g,r = cv2.split(image)
print(r)
print(g)
print(b)

empty = np.zeros(image.shape[:2],dtype = "uint8")
blue = cv2.merge([b,empty,empty])
green = cv2.merge([empty,g,empty])
red = cv2.merge([empty,empty,r])


cv2.imshow("sample image", image)
cv2.imshow("Red",red)
cv2.imshow("Blue",blue)
cv2.imshow("Green",green)

cv2.waitKey()
