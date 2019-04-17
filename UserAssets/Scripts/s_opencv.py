from UserAssets.Scripts.basics import *
import numpy as np
import cv2


cap = None
sprtie = None
fc, ec = None, None
lv1, lv2 = None, None
transform = Transform2D()


def Start():
    global fc, ec, lv1, lv2, cap, sprtie

    lv1 = instantiate_script('point')
    lv2 = instantiate_script('point')

    ec = cv2.CascadeClassifier('UserAssets/Others/haarcascade_eye.xml')
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

    left, right = GetEyesLocation(frame, frame.shape)

    if left and right:
        lv1.transform.position = lerp(left,  lv1.transform.position, Time.deltaTime)
        lv2.transform.position = lerp(right, lv2.transform.position, Time.deltaTime)
    else:
        lv1.transform.position = Vector3(0, 0, 10)
        lv2.transform.position = Vector3(0, 0, 10)




def GetEyesLocation(frame, shape):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = fc.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 1:
        face = faces[0]
        x, y, w, h = face
        face_bytes = gray[y:y+h, x:x+w]

        eyes = ec.detectMultiScale(face_bytes, 1.3, 5)

        if len(eyes) == 2:
            left_x = transform.scale.x * ((x + eyes[0][0] + eyes[0][2] / 2) - (shape[1] / 2)) / 50
            left_y = transform.scale.y * ((shape[0] / 2) - (y + eyes[0][1] + eyes[0][3] / 2)) / 50

            right_x = transform.scale.x * ((x + eyes[1][0] + eyes[1][2] / 2) - (shape[1] / 2)) / 50
            right_y = transform.scale.y * ((shape[0] / 2) - (y + eyes[1][1] + eyes[1][3] / 2)) / 50

            if left_x < right_x:
                return Vector3(left_x, left_y, -1), Vector3(right_x, right_y, -1)
            return Vector3(right_x, right_y, -1), Vector3(left_x, left_y, -1)

    return None, None
