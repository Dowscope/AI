#!/usr/bin/python3

import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    frame_with_box = cv.rectangle(frame, (100, 100), (200, 200), (0, 255, 0), 2)
    cv.imshow('frame_with_box', frame_with_box)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()