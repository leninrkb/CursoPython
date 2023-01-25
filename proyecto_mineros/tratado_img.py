import cv2 as cv
import numpy as np

PATH=''
DIR=''

# lectura
img = cv.imread('img_0_4_lenin.jpg')
cv.imshow('original',img)
j = img.shape[1] #columnas
i = img.shape[0] #filas

# traslacion
M = np.float32([[1,0,100],[0,1,100]])
nimg = cv.warpAffine(img,M,(i,j))
cv.imshow('traslacion',nimg)


# rotacion
M = cv.getRotationMatrix2D((i//2, j//2),15,1)
nimg = cv.warpAffine(img, M, (i,j))
cv.imshow('rotacion',nimg)

# escalar
nimg = cv.resize(img, (38,38), interpolation=cv.INTER_CUBIC)
cv.imshow('escalar',nimg)


cv.waitKey(0)
cv.destroyAllWindows()