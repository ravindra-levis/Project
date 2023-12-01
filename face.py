##Webcam Image:
import cv2
from random import randrange
trained_face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret,img = cap.read()
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face=trained_face.detectMultiScale(img)
    print(face)

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y) , (x+w, y+h),(randrange(256),randrange(256),randrange(256)),2)

    cv2.imshow("Clever Imag is",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()
print("Code Complete")

#Upload Img:
# import cv2
# from random import randrange
# trained_face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img=cv2.imread('download.jpg')
# img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# face=trained_face.detectMultiScale(img)
# print(face)

# for (x,y,w,h) in face:
#     cv2.rectangle(img,(x,y) , (x+w, y+h),(randrange(256),randrange(256),randrange(256)),2)

# cv2.imshow("Clever Imag is",img)
# cv2.waitKey()