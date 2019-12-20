import cv2
import numpy as np
import matplotlib.pyplot as plt
import modi
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def make_coordinates(image, line_parameters):
  slope, intercept = line_parameters
  y1 = image.shape[0]
  y2 = int(y1*(2/5))
  x1 = int((y1 - intercept)/slope)
  x2 = int((y2 - intercept)/slope)
  return np.array([x1, y1, x2, y2])

def average_slope_intercept(image, lines):
  left_fit = []
  right_fit = []
  for line in lines:
    x1, y1, x2, y2 = line.reshape(4)
    parameters = np.polyfit((x1, x2), (y1, y2), 1)
    slope = parameters[0]
    intercept = parameters[1]
    if slope < -0.5:
      left_fit.append((slope, intercept))
    elif 0.5 < slope:
      right_fit.append((slope, intercept))
  if (len(left_fit) != 0):
    left_fit_average = np.average(left_fit, axis=0)
  else:
    left_fit_average = ((1, 10))
  if (len(right_fit) != 0):
    right_fit_average = np.average(right_fit, axis=0)
  else:
    right_fit_average = ((1, 10))
  left_line = make_coordinates(image, left_fit_average)
  rigth_line = make_coordinates(image, right_fit_average)
  return np.array([left_line, rigth_line])

def canny(image):
  gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
  blur = cv2.GaussianBlur(gray, (5, 5), 0)
  canny = cv2.Canny(blur, 50, 150)
  return canny

def display_lines(image, lines):
  line_image = np.zeros_like(image)
  if lines is not None:
    for x1, y1, x2, y2 in lines:
      cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
  return line_image

def t_display_lines(image, lines):
  line_image = np.zeros_like(image)
  if lines is not None:
    for line in lines:
      x1, y1, x2, y2 = line.reshape(4)
      cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
  return line_image

def region_of_interest(image):
  height = image.shape[0]
  polygons = np.array([[(100, height), (600, height), (500, 300), (120,300)]])
  mask = np.zeros_like(image)
  cv2.fillPoly(mask, polygons, 255)
  masked_image = cv2.bitwise_and(image, mask)
  return masked_image

def find_vanishing(image, lines):
  x11, y11, x12, y12 = lines[0]
  x21, y21, x22, y22 = lines[1]
  m1 = (y12 - y11) / (x12 - x11)
  m2 = (y22 - y21) / (x22 - x21)
  cx = int((x11 * m1 - y11 - x21 * m2 + y21) / (m1 - m2))
  center = int((x11+x21)/2)

  cv2.line(image, (cx, 0), (cx, image.shape[0]), (0, 0, 255), 10) 
  cv2.putText(image, str(cx), (cx+10, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
  cv2.line(image, (center, 0), (center, image.shape[0]), (0, 255, 0), 10)
  cv2.putText(image, str(center), (center+10, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

  return image, cx, center

def find_num(image, canny):
  _, contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  MIN_AREA = 50
  MAX_AREA = 5000
  MIN_RATIO, MAX_RATIO = 0.5, 1.0
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
      if ((center_x-dt) > 200) and (center_x < 600) and ((center_y-dt) > 400) and (center_y < 1000):
        img = image[center_y-dt:center_y+dt, center_x-dt:center_x+dt]
        number = process(img)  
      cv2.rectangle(image, pt1=(center_x - 50, center_y - 50), pt2=(center_x + 50, center_y + 50), color=(0, 255, 0), thickness=2)
      cv2.putText(image, "Number", (x+w, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    else:
      cv2.rectangle(image, pt1=(x, y), pt2=(x+w, y+h), color=(255, 0, 0), thickness=2)
      cv2.putText(image, "No", (x+w, y), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
  cv2.imshow('res', image)
  return number

def find_way(vanishing, center):
  diff = vanishing - center
  print(diff)
  if diff < -70:
    left()
  elif diff > 70:
    right()
  else:
    forward()

# Initialize MazeRunner, gets MODI class
# Add needed modules
def init_MR(bundle):
  print('modules list\n', bundle.modules)
  motor = bundle.motors[0]
  return len(bundle.modules), motor

# Checks module connection status by comparing module numbers.
def is_connected(curr_num):
  if curr_num != module_num:
    print('\n--------interrupt!!!---------')
    print('Some modules disconnected!!')
    return False
  else:
    return True

# MODI goes forward, gets delay, speed args
def forward(delay=3, speed=100):
  motor.speed(0, 0)
  time.sleep(0.001)
  # if button.clicked() == True:
  print('-----forward!!-----')
  for _ in range(delay):
    # mazeprint(ir.distance())
    time.sleep(0.001)
    motor.speed(speed, -speed)
    time.sleep(0.001)
  motor.speed(0, 0)

# MODI turns left, gets delay arg.
def left(delay=1):
  motor.speed(0, 0)
  time.sleep(0.001)
  print('-----left!!-----')
  for _ in range(delay):
    time.sleep(0.001)
    motor.speed(-100, -100)
    time.sleep(0.001)
  motor.speed(0, 0)

# MODI turns right, gets delay arg.
def right(delay=1):
  motor.speed(0, 0)
  time.sleep(0.001)
  print('-----right!!-----')
  for _ in range(delay):
    time.sleep(0.001)
    motor.speed(100, 100)
    time.sleep(0.001)
  motor.speed(0, 0)


msg_cnt = 100 
def mazeprint(msg, arg=None):
  global msg_cnt
  db = firestore.client()
  doc_ref = db.collection(u'Maze').document(str(msg_cnt))
  if arg:
    print(msg, arg)
    doc_ref.set({
      u'Text': str(msg) + " " + str(arg)
    })
  else:
    print(msg)
    doc_ref.set({
      u'Text': msg
    })
  msg_cnt = msg_cnt + 1

def delete_collection(coll_ref, batch_size):
  docs = coll_ref.limit(batch_size).get()
  deleted = 0

  for doc in docs:
    print(u'Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
    doc.reference.delete()
    deleted = deleted + 1

  if deleted >= batch_size:
    return delete_collection(coll_ref, batch_size)

if __name__=="__main__":
  # Initialize
  cred = credentials.Certificate("./AccountKey.json")
  firebase_admin.initialize_app(cred)
  delete_collection(firestore.client().collection(u'Maze'), 200)
  bundle = modi.MODI()
  time.sleep(1)
  module_num, motor = init_MR(bundle)
  time.sleep(1)
  print('MODI Connected!')

  # Main
  cap = cv2.VideoCapture(-1)
  while(cap.isOpened()):
    time.sleep(0.01)
    _, frame = cap.read()
    canny_image = canny(frame)
    cropped_image = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=3)
    if len(lines) < 2:
      continue
    averaged_lines = average_slope_intercept(frame, lines)
    find_vanishing(frame, averaged_lines)
    line_image = t_display_lines(frame, averaged_lines)
    vanishing_line, vanishing, center = find_vanishing(line_image, averaged_lines)
    combo_image = cv2.addWeighted(frame, 0.8, vanishing_line, 1, 1)
    find_way(vanishing, center)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  cap.release()
  cv2.destroyAllWindows()
