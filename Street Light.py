import cv2
import cvzone
#import pyttsx3
from cvzone.FaceMeshModule import FaceMeshDetector
cap = cv2.VideoCapture(1)
detector = FaceMeshDetector (maxFaces=2)
#engine = pyttsx3.init('sapi5')
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)

while True:
    success, img = cap.read()
    #chk = True
    img, faces = detector.findFaceMesh(img, draw=False)
    if faces:
        face = faces [0]
        pointLeft = face [145]
        pointRight = face [374]
        w, _ = detector.findDistance (pointLeft, pointRight)
        W = 6.3
        f = 390
        d = (W * f) / w
        #if d <100 and chk == True:
            #engine.say("hellow")
           # engine.runAndWait()
        #chk = False
        cvzone.putTextRect(img, f'Depth: {int(d)}cm',(face[10][0] - 100, face[10][1] - 50),scale=2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
    cv2.imshow("Image", img)
    cv2.waitKey(1)