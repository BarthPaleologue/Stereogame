import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from geometry import OBJ

class Bomb(OBJ):
    def __init__(self) :
        OBJ.__init__(self,"./Bomb.obj")

    