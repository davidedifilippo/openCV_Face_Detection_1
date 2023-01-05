import cv2
import serial
import time

face_cascade = cv2.CascadeClassifier('Risorse/haarscascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("Width:", width)
print("Height:", height)

serialPort = serial.Serial('/dev/cu.usbmodem103', 9600, timeout=0.1)

time.sleep(1)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # mirror the image
    # print(frame.shape)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 6)  # detect the face

    for x, y, w, h in faces:
        # sending coordinates to Arduino
        string = 'X{0:d}Y{1:d}'.format((x+w//2), (y+h//2))
        print(string)
        serialPort.write(string.encode('utf-8'))
        # plot the center of the face

        cv2.circle(frame, (x+w//2, y+h//2), 2, (0, 255, 0), 2)

        # plot the roi

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # plot the squared region in the center of the screen

    cv2.rectangle(frame, (int(width)//2-30, int(height)//2-30), (int(width)//2+30, int(height)//2+30), (0, 255, 0), 2)

    # out.write(frame)

    cv2.imshow('img', frame)

    # press q to Quit

    if (cv2.waitKey(10) & 0xFF) == ord('q'): # only the first 8 bit
        break

cap.release()
cv2.destroyAllWindows()

