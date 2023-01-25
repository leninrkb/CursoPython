import cv2
# funciona piola 1 (scaleFactor = 5, minNeighbors = 12, minSize=(38,38))
# face_cascade = cv2.CascadeClassifier('modelos/mod_ca_1.xml')

# funca re piola (scaleFactor = 5, minNeighbors = 12, minSize=(38,38))
face_cascade = cv2.CascadeClassifier('modelos/mod_ca_2.xml')

# no sirve
# face_cascade = cv2.CascadeClassifier('modelos/mod_ca_3.xml')

cap = cv2.VideoCapture(0)

while (True):
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 5, minNeighbors = 20, minSize=(38,38))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30)
    if k == 27: 
        break
cap.release()
cv2.destroyAllWindows()