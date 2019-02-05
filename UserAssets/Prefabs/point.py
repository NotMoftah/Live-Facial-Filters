from UserAssets.Scripts.basics import *
import numpy as np
import cv2

sprtie = SpriteRenderer('point.png')
transform = Transform2D()


def Start():
    transform.scale = Vector3(0.1, 0.1, 0.1)

    
def Render():
    transform.applyTransformation()
    sprtie.render()
