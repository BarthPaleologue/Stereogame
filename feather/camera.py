import numpy as np
from feather.algebra import rotate
from feather.projections import perspective

class Camera():
    def __init__(self, fov, aspectRatio):
        self.projection = perspective(fov, aspectRatio, 0.1, 100)
        self.rotation = np.array([0, 0, 0])

    def setRotationX(self, angle):
        self.rotation[0] = angle
    
    def setRotationY(self, angle):
        self.rotation[1] = angle

    def setRotationZ(self, angle):
        self.rotation[2] = angle

    def getRotationMatrix(self):
        return rotate(self.rotation[0], 1.0, 0.0, 0.0).dot(
            rotate(self.rotation[1], 0.0, 1.0, 0.0)
        ).dot(rotate(self.rotation[2], 0.0, 0.0, 1.0))

    def getProjectionMatrix(self):
        return self.getRotationMatrix().dot(self.projection)