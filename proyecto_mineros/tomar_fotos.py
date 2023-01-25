import cv2
import numpy as np 
import imutils 
import os 
import time


# Datos = 'n'
# if not os.path.exists(Datos):
#     print('carpeta creada: ',Datos)
#     os.makedirs(Datos) 
OUT_PATH='D:/datasets/cuasapas_data/chaleco/nuevo_data_38/n'

cap = cv2.VideoCapture(0)
x1, y1 = 200, 80
x2, y2 = x1+300, y1+300
count=531
while (True):
    ret, frame = cap.read()
    if ret == False: break 
    aux = frame.copy()
    cv2.rectangle(frame, (x1,y1), (x2, y2), (255,0,0), 2)
    objeto = aux[y1:y2,x1:x2]
    objeto = imutils.resize(objeto, width=38)
    cv2.imshow('frame',frame)
    cv2.imshow('objeto',objeto)
    k=cv2.waitKey(1)
    if k == 27: break 
    # time.sleep(0.3)
    if k == ord('s'): 
        Datos='{}/imgp_{}.jpg'.format(OUT_PATH,count)
        cv2.imwrite(Datos, objeto)
        count+=1
cap.release()
cv2.destroyAllWindows()