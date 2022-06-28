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

    def translate(self, x, y, z):
        self.position[0] += x
        self.position[1] += y
        self.position[2] += z

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

    def setRotationAxisAround(self, angle, axisX, axisY, axisZ, x, y, z):
        position4 = np.array([self.position[0], self.position[1], self.position[2], 1.0])
        rotatedPosition4 = rotate(angle, axisX, axisY, axisZ).dot(position4)
        self.position = np.array([rotatedPosition4[0], rotatedPosition4[1], rotatedPosition4[2]])
        self.translate(x, y, z)

    def setRotationXAround(self, angle, x, y, z):
        self.setRotationAxisAround(angle, 1.0, 0.0, 0.0, x, y, z)

    def setRotationYAround(self, angle, x, y, z):
        self.setRotationAxisAround(angle, 0.0, 1.0, 0.0, x, y, z)

    def setRotationZAround(self, angle, x, y, z):
        self.setRotationAxisAround(angle, 0.0, 0.0, 1.0, x, y, z)

    """Sets the rotation of the object along each world axis"""
    def setRotation(self, xAngle, yAngle, zAngle):
        self.rotation[0] = xAngle
        self.rotation[1] = yAngle
        self.rotation[2] = zAngle
        return self

    """Sets the object's rotation around the world X axis and returns the object"""
    def setRotationX(self, angle):
        self.rotation[0] = angle
        return self
    
    """Sets the object's rotation around the world Y axis and returns the object"""
    def setRotationY(self, angle):
        self.rotation[1] = angle
        return self

    """Sets the object's rotation around the world Z axis and returns the object"""
    def setRotationZ(self, angle):
        self.rotation[2] = angle
        return self

    """Adds to the object's rotation around each world axis and returns the object"""
    def addRotation(self, xAngle, yAngle, zAngle):
        self.rotation[0] += xAngle
        self.rotation[1] += yAngle
        self.rotation[2] += zAngle
        return self

    """Adds to the object's rotation around the world X axis and returns the object"""
    def addRotationX(self, angle):
        self.rotation[0] += angle
        return self

    """Adds to the object's rotation around the world Y axis and returns the object"""
    def addRotationY(self, angle):
        self.rotation[1] += angle
        return self

    """Adds to the object's rotation around the world Z axis and returns the object"""
    def addRotationZ(self, angle):
        self.rotation[2] += angle
        return self

    def getRotationMatrix(self):
        #TODO: use a cache system to reduce computations
        return rotate(self.rotation[0], 1.0, 0.0, 0.0).dot(
                rotate(self.rotation[1], 0.0, 1.0, 0.0)).dot(
                rotate(self.rotation[2], 0.0, 0.0, 1.0))

    def getMatrix(self):
        return self.getRotationMatrix().dot(self.getPositionMatrix()).dot(self.getScalingMatrix())
