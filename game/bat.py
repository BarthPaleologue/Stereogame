import os
import pygame
from OpenGL.GL import *
import numpy as np

from feather.shapes.shape import Shape
from feather.loaders import RowOBJ

class Bat(RowOBJ):

    def __init__(self, filename, swapyz=False, scene=None):
        RowOBJ.__init__(self, filename, swapyz, scene)
        self.position = np.array([0.0, 0.0, 0.0])
        self.velocity = np.array([0.0, 0.0, 0.0])
        self.ends = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        self.radius = 0

    def strike(self):#a finir
        self.translate(self.velocity[0], self.velocity[1], self.velocity[2])
        self.setRotationXAround(5, 10, 20, 30)
     #   newVelocity = np.array([self.velocity[0]+self.acceleration[0], self.velocity[1]+self.acceleration[1], self.velocity[2]+self.acceleration[2]])  
      #  self.velocity = newVelocity

    def move(self):
        self.translate(self.velocity[0], self.velocity[1], self.velocity[2])
        newVelocity = np.array([self.velocity[0]+self.acceleration[0], self.velocity[1]+self.acceleration[1], self.velocity[2]+self.acceleration[2]])  
        self.velocity = newVelocity
        
    def setVelocity(self, x, y, z):
        self.velocity = np.array([x, y, z])

    def getVelocity(self):
        return self.velocity

    def setAcceleration(self, x, y, z):
        self.acceleration = np.array([x, y, z])

    def getAcceleration(self):
        return self.acceleration

    def setRadius(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius

    def setEnds(self, ends):
        self.ends = ends
    
    def getEnds(self):
        futurePosition = np.array([self.position[0]+self.velocity[0], self.position[1]+self.velocity[1], self.position[2]+self.velocity[2]])
        ends = np.add(self.vertices, np.full((len(self.vertices), 3), futurePosition))
        return ends

