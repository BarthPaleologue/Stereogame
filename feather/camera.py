import numpy as np
from feather.transform import Transform
from feather.algebra import rotate
from feather.projections import perspective

class Camera(Transform):
    def __init__(self, fov, aspectRatio):
        Transform.__init__(self)
        self.projection = perspective(fov, aspectRatio, 0.1, 100)

    def getProjectionMatrix(self):
        return self.getRotationMatrix().dot(self.projection)