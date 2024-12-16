import cv2 as cv 

capture = cv.VideoCapture(0) 
face_casceide = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
    ret, frame = capture.read() 
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face = face_casceide.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )
    for (x,y,w,h) in face:
        cv.rectangle(frame,(x,y), (x+w,y+h),(0,255,0))
        cv.flip(frame,0) 
    cv.imshow('video',frame)
    if cv.waitKey(1) & 0xFF ==  ord('q'):
        break 

capture.release() 
cv.destroyAllWindows() 

