from OpenGL.GL import *
import numpy as np
from pygame.math import Vector3
import pygame

#local imports
from feather.camera import Camera
from feather import FrameBuffer
from feather.algebra import *

class Eye(Camera):
    def __init__(self):
        #infoObject = pygame.display.Info()
        #width, height = infoObject.current_w, infoObject.current_h
        width, height = 1920, 1080
        Camera.__init__(self, 45, width/height)
        
        self.frameBuffer = FrameBuffer(int(width/4), int(height/4))

    def getFrameBuffer(self) :
        return self.frameBuffer

    def setFrameBuffer(self, frameBuffer) :
        self.frameBuffer = frameBuffer