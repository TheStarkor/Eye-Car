import cv2
import numpy as np

image = 't1.jpg'

gray = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

cv2.imshow('res', gray)
cv2.waitKey(0)

print(gray.shape)
