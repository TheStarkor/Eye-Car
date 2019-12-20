import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 1080)

while True:
  ret, frame = cap.read()
  cv2.imshow('test', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()

cv2.destroyAllWindows()