import numpy as np 
import cv2 as cv 
import sys
class analise:
    def exibindo_video_img(self,video,img):
        self.img = img
        cap = cv.VideoCapture("video1.avi")
        while cap.isOpened():
            ret,frame = cap.read()
            # Caso o câmera não abrir 
            if not ret:
                break 
            gray = cv.cvtColor(frame,cv.COLOR_BAYER_BG2BGR)
            cv.imshow('frame',gray)
            if cv.waitKey(1) == ord("q"):
                break 
            cap.release()
            cv.destroyAllWindows()
        img = cv.imread(cv.samples.findFile("foto.png"))
        if img is None:
            sys.exit("Imagem inexistente")
        cv.imshow("mostrar janela",img)
        quit = cv.waitKey(0)
        if quit == "q":
            cv.imwrite("foto.png",img)

    def analise_video():
        pass 

    def analise_img():
        pass 
