import cv2

faceCascade = cv2.CascadeClassifier("Risorse/haarscascade_frontalface_default.xml")
img = cv2.imread("Risorse/lena.png")

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(grayImg, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("lena", img)
cv2.waitKey(10000)
