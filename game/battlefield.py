from feather.shapes import Cube


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
    
    

    def isCollision(self,r,x,y,z): # cette fonction prend en paramètres un poins dans l'espace
                            # et renvoie True s'il y a collision entre ce point et la battlefield
        if x+r == self.size_x or x-r == -self.size_x:
            return True
        elif y+r == self.size_y or y-r == -self.size_y:
            return True
        elif z+r == self.size_z or z-r == -self.size_z:
            return True
        else:
            return False

    def whereCollision(self,r,x,y,z):
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
    
    
    



