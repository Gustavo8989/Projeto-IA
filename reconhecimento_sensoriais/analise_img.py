import cv2 as cv
import numpy as np 
import mahotas
# Contar os lados do dados que estão para cima 
imagem_colorida = cv.imread("Imagens/img02.png")

def escrever(imagem,texto,cor=(255,0,0)):
    fonte = cv.FONT_HERSHEY_SIMPLEX 
    cv.putText(imagem,texto,(10,20),fonte,0.5, cor, 0, cv.LINE_AA) 

imagem = cv.cvtColor(imagem_colorida, cv.COLOR_BGR2GRAY)
suave = cv.blur(imagem,(7,7)) 

# Binarização da imagem, resultando em pixel branco e preto 
T = mahotas.thresholding.otsu(suave)
bin = suave.copy() 
bin[bin > T] = 255 
bin[bin < 255] = 0
bin = cv.bitwise_not(bin) 

bordas = cv.Canny(suave,70,150) 




cv.imshow("Quantidade de objetos",bordas) 
cv.waitKey(0) 

