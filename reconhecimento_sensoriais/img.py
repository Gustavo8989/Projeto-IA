import cv2 as cv
import numpy as np 
import face_recognition

# Contar os lados do dados que estão para cima 
imagem_bebe = cv.imread("Imagens/bebe.webp")



cv.imshow("Quantidade de objetos",imagem_bebe) 
cv.waitKey(0) 

