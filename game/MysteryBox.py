from feather.shapes.cube import Cube

class MysteryBox(Cube):
    def __init__(self,name, scene = None):
        Cube.__init__(self, name,False, scene)
        
