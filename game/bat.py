import os
import pygame
from OpenGL.GL import *
import numpy as np

from feather.shapes.shape import Shape
from feather.loaders import RowOBJ
from feather.materials import TextureMaterial
from feather import Texture

class Bat(RowOBJ):

    def __init__(self, filename, scene=None):
        RowOBJ.__init__(self, filename, False, scene)
        self.position = np.array([0.0, 0.0, 0.0])
        self.velocity = np.array([0.0, 0.0, 0.0])
        self.ends = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        self.radius = 2
        self.counter = 0
        self.isStriking = False
        self.beginZ = 50
        self.beginY = 30
        self.endZ = 50
        self.endY = -40
        self.state = 0
        self.animationDuration = 0.2
        self.batReturn = False

        batMat = TextureMaterial(Texture("./assets/baseball/wood.jpg"))
        self.setMaterial(batMat)

        self.setScaling(0.7, 0.7, 0.7)

    def strike(self):
            self.isStriking = True

    def update(self, deltaTime) :
        if self.isStriking :
            self.state = self.counter/self.animationDuration
            self.setRotation(0, self.state*self.endY + (1-self.state)*self.beginY, self.state*self.endZ + (1-self.state)*self.beginZ)

            if self.state<=1 and not self.batReturn:
                self.counter += deltaTime
            if self.state > 1 or self.batReturn:
                self.batReturn = True
                self.counter -= deltaTime
                if self.state<=0:
                    self.isStriking = False
                    self.batReturn = False

        
    def setVelocity(self, x, y, z):
        self.velocity = np.array([x, y, z])

    def getVelocity(self):
        return self.velocity

    def setRadius(self, radius):
        self.radius = radius

    def setStriking(self, state):
        self.isStriking = state
    
    def getRadius(self):
        return self.radius

    def setEnds(self, ends):
        self.ends = ends
    
    def getEnds(self):
        return self.ends

    def getEndPoint1(self):
        return np.array([9.5, 0, 0])

    def getEndPoint2(self):
        return np.array([-9.5, 0, 0])

