import numpy as np 
import cv2 as cv 

def exibindo_video():
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

exibindo_video()
