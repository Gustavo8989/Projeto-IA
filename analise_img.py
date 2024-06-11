import cv2 as cv 
import numpy as np 
imagem = cv.imread('Imagens/img01.jpg')
(b,g,r) = imagem[0,0]


def analise_img():
    # Modificando a imagem
    for y in range(0, imagem.shape[0]):
        for x in range(0, imagem.shape[1]):
            imagem[y,x] =  (255,0,0)
