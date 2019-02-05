from UserAssets.Scripts.basics import *
import numpy as np
import cv2

sprtie = SpriteRenderer('point.png')
transform = Transform2D()

scale_direction = 1
max_scale = Vector3(0.1, 0.1, 0.1)
min_scale = Vector3(0.01, 0.01, 0.01)

def Start():
    transform.scale = Vector3(0.05, 0.05, 0.05)


def Render():
    transform.applyTransformation()
    sprtie.render()


def Update():
    global scale_direction
    if transform.scale.squareMagnitude() + 0.01 > max_scale.squareMagnitude():
        scale_direction = -1

    if transform.scale.squareMagnitude() < min_scale.squareMagnitude() + 0.01:
        scale_direction = +1

    transform.scale = lerp(transform.scale, max_scale if scale_direction > 0 else min_scale, Time.deltaTime)
