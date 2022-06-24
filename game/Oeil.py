from OpenGL.GL import *
import numpy as np
from pygame.math import Vector3

#local imports
from feather.camera import *

class Oeil :

    def __init__(self, frameBuffer, view_matrix, position, eye_target) :
        self.frameBuffer = frameBuffer
        self.view_matrix = view_matrix
        self.position = position
        self.eye_target = eye_target
    #position espace (vetc3)
    #eye target (vect3)

    def getFrameBuffer(self) :
        return self.frameBuffer

    def getView_Matrix(self) :
        return self.view_matrix

    def setPosition(self, x, y, z) :
        self.position = Vector3(x, y, z)
    
    def getPosition(self) :
        return self.position

    def setEye_Target(self, x, y ,z) :
        self.eye_target = Vector3(x, y, z)
    
    def getEye_Target(self) :
        return self.eye_target
        