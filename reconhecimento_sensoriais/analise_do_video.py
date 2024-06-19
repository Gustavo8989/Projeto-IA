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
            cap.release()
            cv.destroyAllWindows()
        frame_array = np.array(frame)
    def redinencionamndo_img():
        pass 
analise()
