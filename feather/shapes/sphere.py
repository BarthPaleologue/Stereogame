from feather.shapes.cube import Cube

class Sphere(Cube):
    def __init__(self, name, flip, scene=None):
        super().__init__(name, flip, scene)