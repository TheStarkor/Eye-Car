import tensorflow as tf
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def canny(image):
  gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
  blur = cv2.GaussianBlur(gray, (5, 5), 0)
  canny = cv2.Canny(blur, 50, 150)
  return canny

def contour(image, canny):
  contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  cv2.drawContours(image, contours, -1, (0, 0, 255), 1)

def find_num(image, canny):
  _, contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  MIN_AREA = 50
  MAX_AREA = 5000
  MIN_RATIO, MAX_RATIO = 0.2, 1.0
  MIN_HEIGHT = 10
  dt = 50
  number = 10

  for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    area = w * h
    ratio = w / h

    if MIN_AREA < area < MAX_AREA \
    and MIN_RATIO < ratio < MAX_RATIO \
    and MIN_HEIGHT < h:
      center_x = int((2 * x + w) / 2)
      center_y = int((2 * y + h) / 2)
      img = image[center_y-dt:center_y+dt, center_x-dt:center_x+dt]
      # number = process(img)
      cv2.imshow('find', img)
      cv2.rectangle(image, pt1=(center_x - 50, center_y - 50), pt2=(center_x + 50, center_y + 50), color=(0, 255, 0), thickness=2)
      cv2.putText(image, "Number", (x+w, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    else:
      cv2.rectangle(image, pt1=(x, y), pt2=(x+w, y+h), color=(255, 0, 0), thickness=2)
      cv2.putText(image, "No", (x+w, y), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
  if (number != 10): 
    print('The number is: ', number)
  cv2.imshow('res', image)

def region_of_interest(image):
  height = image.shape[0]
  polygons = np.array([[(300, 300), (400, 300), (400, 200), (300, 200)]])
  mask = np.zeros_like(image)
  cv2.fillPoly(mask, polygons, 255)
  masked_image = cv2.bitwise_and(image, mask)
  return masked_image

def process(img):
  global model
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray = cv2.resize(gray, (28,28), interpolation=cv2.INTER_AREA)
  gray = gray.astype('float32') / 255
  gray = 1 - gray
  gray = (gray > 0.2) * gray
  predictions = model.predict(gray[np.newaxis,:])
  a = tf.math.argmax(predictions, 1)
  print('Answer',tf.keras.backend.eval(a)[0])
  return tf.keras.backend.eval(a)[0]

# for video
cap = cv2.VideoCapture(-1)
while (cap.isOpened()):
  _, frame = cap.read()
  load_image = np.copy(frame)
  canny_image = canny(load_image)
  cropped_image = region_of_interest(canny_image)
  find_num(load_image, cropped_image)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
