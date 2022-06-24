from OpenGL.GL import *
import numpy as np
from pygame.math import Vector3
import pygame

#local imports
from feather.camera import *
from feather import FrameBuffer
from feather.algebra import *

class Eye:

    def __init__(self, position, eye_target) :
        infoObject = pygame.display.Info()
        width, height = infoObject.current_w, infoObject.current_h
        self.frameBuffer = FrameBuffer(int(width/2), int(height/2))
        self.view_matrix = lookat(position, eye_target)
        self.position = position
        self.eye_target = eye_target
    #position espace (vetc3)
    #eye target (vect3)

    def getFrameBuffer(self) :
        return self.frameBuffer

    def setFrameBuffer(self, frameBuffer) :
        self.frameBuffer = frameBuffer

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
        