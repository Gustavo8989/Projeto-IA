import numpy as np 
import cv2 as cv 

def captura_camera():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Erro com a câmera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret: 
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'): 
            break
    cap.release()
    cv.destroyAllWindows()
captura_camera()

