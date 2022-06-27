from feather.shapes import Cube
import numpy as np


class Battlefield(Cube):
    
    def __init__(self, name, size_x, size_y, size_z, scene = None):
        self.size_x = size_x
        self.size_y = size_y
        self.size_z= size_z
        Cube.__init__(self, name, False, scene)
        self.setScaling(size_x, size_y, size_z)

    def getSizex(self):
        return self.size_x

    def getSizey(self):
        return self.size_y

    def getSizez(self):
        return self.size_z
    
    

    def isCollision(self,r,center): # cette fonction prend en paramètres un poins dans l'espace
                            # et renvoie True s'il y a collision entre ce point et la
                            #  battlefield
        x,y,z = center[0], center[1], center[2]
        if x+r == self.size_x or x-r == -self.size_x:
            return True
        elif y+r == self.size_y or y-r == -self.size_y:
            return True
        elif z+r == self.size_z or z-r == -self.size_z:
            return True
        else:
            return False

    def whereCollision(self,r, center):
        x,y,z = center[0], center[1], center[2]
        if x+r == self.size_x:
            return "right"
        elif x-r == -self.size_x:
            return "left"
        elif y+r == self.size_y:
            return "top"
        elif y-r == -self.size_y:
            return "bottom"
        elif z+r == self.size_z:
            return "front"
        elif z-r == -self.size_z:
            return "back"
        else:
            return "No Collision"

    def normalVector(self, face):
        if face == "right":
            return np.array([-1,0,0]), np.array([0,1,1])
        elif face == "left":
            return np.array([1,0,0]), np.array([0,1,1])
        elif face == "top":
            return np.array([0,-1,0]), np.array([1,0,1])
        elif face == "bottom":
            return np.array([0,1,0]), np.array([1,0,1])
        elif face == "front":
            return np.array([0,0,-1]), np.array([1,1,0])
        elif face == "back":
            return np.array([0,0,1]), np.array([1,1,0])
        else:
            return np.array([0,0,0]), np.array([0,0,0])
        
    
    
    



