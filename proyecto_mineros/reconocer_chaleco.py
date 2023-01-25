import cv2
# no sirve
# chaleco = cv2.CascadeClassifier('modelos/mod_ch_13et.xml')


# mal
# chaleco = cv2.CascadeClassifier('modelos/mod_ch_15et.xml')


# ni hablar
# chaleco = cv2.CascadeClassifier('modelos/mod_ch_18et.xml')

# no funciona
# chaleco = cv2.CascadeClassifier('modelos/mod_ch_15et_2.xml')

# no
# chaleco = cv2.CascadeClassifier('modelos/mod_ch_15et_3.xml')

chaleco = cv2.CascadeClassifier('modelos/cascade_aumdata_13.xml')

cap = cv2.VideoCapture(0)

while (True):
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    chalecos = chaleco.detectMultiScale(gray, scaleFactor = 10, minNeighbors = 90, minSize=(38,38))
    for (x, y, w, h) in chalecos:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.putText(img,'chaleco',(x,y),2,0.7,(255,0,0),2,cv2.LINE_AA)
    cv2.imshow('img',img)
    k = cv2.waitKey(30)
    if k == 27: 
        break
cap.release()
cv2.destroyAllWindows()