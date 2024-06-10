import numpy as np 
import cv2 as cv 
import sys

contar_pessoas = 0

class analise:
    def exibindo_video_img():
        cap = cv.VideoCapture("video1.avi")
        while cap.isOpened():
            ret,frame = cap.read()
            # Caso o câmera não abrir 
            if not ret:
                break 
            gray = cv.cvtColor(frame,cv.COLOR_BAYER_BG2BGR)
            cv.imshow('Video',gray)
            if cv.waitKey(1) == ord("q"):
                break 
            frame.append(gray)
            # Detectando Pessoas 
            _,limite = cv.threshold()
            cap.release()
            cv.destroyAllWindows()
        frame_array = np.array(frame)


analise()
#https://professor.luzerna.ifc.edu.br/ricardo-antonello/wp-content/uploads/sites/8/2017/02/Livro-Introdução-a-Visão-Computacional-com-Python-e-OpenCV-3.pdf