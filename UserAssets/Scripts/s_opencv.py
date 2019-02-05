from UserAssets.Scripts.basics import *
import numpy as np
import cv2


cap = None
sprtie = None
transform = Transform2D()

def Start():
    global cap, sprtie

    transform.scale = Vector3(1, -1, -1)

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    sprtie = RawBytesSpriteRenderer(frame, frame.shape)


def Render():
    transform.applyTransformation()
    sprtie.render()


def Update():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    sprtie.update_bytes(frame)

    if Input.KeyDown('q'):
        cap.release()
        cv2.destroyAllWindows()
