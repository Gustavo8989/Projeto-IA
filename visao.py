import numpy as np
import cv2 as cv

def captura_camera():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao abrir a câmera")
        return
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('video1.avi', fourcc, 20.0, (480, 640))
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar frame")
            break
        frame = cv.flip(frame, 1)
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()

captura_camera()

