import numpy as np
import cv2
import os

path = "C:/Users/mrseb/OneDrive/Bureau/DroneTracker/dataBase"

cap = cv2.VideoCapture(0)

count = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    count += 1
    if ret==True:

        name = "photo " + str(count) + ".jpg"
        cv2.imwrite(os.path.join(path, name), frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
