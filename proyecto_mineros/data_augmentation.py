import albumentations as A
import cv2
import os
import matplotlib.pyplot as plt

transform = A.Compose([
    A.RandomRotate90(),
    A.Flip(),
    A.Transpose(),
    A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.1, rotate_limit=45)
])


PATH = 'D:/datasets/cuasapas_data/chaleco/nuevo_data_38'
DIR = ['re']
OUT_PATH='D:/datasets/cuasapas_data/chaleco/nuevo_data_38/aum'
c2=0
# for category in CATEGORIES:
path=os.path.join(PATH, DIR)
for img in os.listdir(path):
    img_array=cv2.imread(os.path.join(pathimg))
    count=0
    while(count<5):
        augmented_image = transform(image=img_array)['image']
        Datos='{}/img_{}_{}.jpg'.format(OUT_PATH,count,c2)
        cv2.imwrite(Datos, augmented_image)
        count+=1
        c2+=1
        
print('total img =',c2)
        
# count=0
# while(count<100):
#     image = cv2.imread(os.path.join('/home/lenin/Downloads/Original/''1.jpg'))
#     augmented_image = transform(image=image)[\image\]
#     Datos='/home/lenin/Documents/GitHub/CursoPython/Cuadernos de Trabajo/Cuadernos de Trabajo/chalecos/img_{}.jpg'.format(count)
#     cv2.imwrite(Datos augmented_image)
#     count+=1
# print('done')
