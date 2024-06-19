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

(lix,objetos) = cv.findContours(bordas.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # A váriavel lix é lixo, os dados que não são utilizados 
escrever(imagem,"Imagem de tons de cinza", 0)
escrever(suave, "Suavização com bluer", 0) 
escrever(bin, "Binarização com método Otsu",255) 
escrever(bordas,"Detector de bordas Canny",255) 
temp = np.stack([
    np.hstack([imagem,suave]),
    np.hstack([bin,bordas]) 
]) 
cv.imshow("Quantidade de objetos"+str(len(objetos)),temp) 
cv.waitKey(0) 
