import numpy as np
from feather.algebra import translate, rotate, scale

class Transform():
    def __init__(self):
        self.position = np.array([0.0, 0.0, 0.0])
        self.scaling = np.array([1.0, 1.0, 1.0])
        self.rotation = np.array([0.0, 0.0, 0.0])

    def setPosition(self, x, y, z):
        self.position[0] = x
        self.position[1] = y
        self.position[2] = z

    def getPosition(self):
        return self.position

    def getPositionMatrix(self):
        return translate(self.position[0], self.position[1], self.position[2])

    def setScaling(self, x, y, z):
        self.scaling[0] = x
        self.scaling[1] = y
        self.scaling[2] = z

    def getScaling(self):
        return self.scaling

    def getScalingMatrix(self):
        return scale(self.scaling[0], self.scaling[1], self.scaling[2])

    def setRotationX(self, angle):
        self.rotation[0] = angle
    
    def setRotationY(self, angle):
        self.rotation[1] = angle

    def setRotationZ(self, angle):
        self.rotation[2] = angle

    def getRotationMatrix(self):
        #TODO: use a cache system to reduce computations
        return rotate(self.rotation[0], 1.0, 0.0, 0.0).dot(
                rotate(self.rotation[1], 0.0, 1.0, 0.0)).dot(
                rotate(self.rotation[2], 0.0, 0.0, 1.0))

    def getMatrix(self):
        return self.getRotationMatrix().dot(self.getPositionMatrix()).dot(self.getScalingMatrix())
