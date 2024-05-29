import numpy as np 
import cv2 as cv 
import sys
class analise:
    def exibindo_video_img(self,video,img):
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
        

    def analise_video():
        pass 

    def analise_img():
        pass 
