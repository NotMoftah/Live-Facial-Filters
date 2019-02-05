from UserAssets.Scripts.basics import *
import numpy as np
import cv2


fc = None
cap = None
sprtie = None
pointer = None
transform = Transform2D()


def Start():
    global fc, cap, sprtie, pointer

    pointer = instantiate_script('point')
    fc = cv2.CascadeClassifier('UserAssets/Others/haarcascade_frontalface.xml')

    cap = cv2.VideoCapture(0)
    ret_dmp, frame = cap.read()
    sprtie = RawBytesSpriteRenderer(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB), frame.shape)


def Render():
    transform.applyTransformation()
    sprtie.render()


def Update():
    global fc, cap

    ret, frame = cap.read()
    bytes = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    sprtie.update_bytes(bytes)

    if Input.KeyDown('q'):
        cap.release()
        cv2.destroyAllWindows()
        quit()

    if Input.KeyDown(' '):
        position = getFace(frame, frame.shape)
        if position:
            pointer.transform.position = position


def getFace(frame, shape):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = fc.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 1:
        face = faces[0]
        x, y, w, h = face
        x = transform.scale.x * (x - (shape[1] / 2)) / 50
        y = transform.scale.y * ((shape[0] / 2) - y) / 50

        return Vector3(x, y, -1)
    return None
