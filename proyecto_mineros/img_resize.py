import cv2
import os

PATH="D:/downloads/jean_img (2)/jean_img"
DIR='jean_img'
OUT_PATH='D:/datasets/cuasapas_data/chaleco/nuevo_data_38/re'

c2=0
path=os.path.join(PATH, DIR)
for img in os.listdir(path):
    img_array=cv2.imread(os.path.join(path,img))
    new_img = cv2.resize(img_array, (38,38), interpolation=cv2.INTER_CUBIC)
    Datos='{}/re_img_{}.jpg'.format(OUT_PATH,c2)
    cv2.imwrite(Datos, new_img)
    c2+=1
        
print('total img =',c2)