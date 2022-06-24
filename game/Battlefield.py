from geometry import *
class Battlefield(Shape):
    def __init__(self, size_x, size_y, size_z, flip = False):
        name = "battlefield"
        Shape.__init__(self, name)
        ty_min = 0.0
        ty_max = 1.0
        if flip == True:
            ty_min = 1.0
            ty_max = 0.0
        
        self.build_buffers(
            [
            ### front face
            ( -size_x, -size_y, size_z), #1
            ( size_x, -size_y, size_z),#2
            ( size_x, size_y, size_z),#3
            ( -size_x, -size_y, size_z),#1
            ( -size_x, size_y, size_z),#4
            ( size_x, -size_y, size_z),#3

            ### back face
            ( -size_x, -size_y, -size_z), #B1
            ( size_x, -size_y, size_z),#B2
            ( size_x, size_y, -size_z),#B3
            ( -size_x, -size_y, -size_z),#B1
            ( -size_x, size_y, -size_z),#B4
            ( size_x, size_y, -size_z),#B3

            ### top face
            (-size_x, size_y, size_z),#4
            (size_x, size_y, size_z),#3
            (size_x, size_y, -size_z),#B3
            (-size_x, size_y, size_z),#4
            (-size_x, size_y, -size_z),#B4
            (size_x, size_y, -size_z),#B3

            ### bottom face
            (-size_x, -size_y, size_z),#1
            (size_x, -size_y, size_z),#2
            (size_x, -size_y, -size_z),#B2
            (-size_x, -size_y, size_z),#1
            (-size_x, -size_y, -size_z),#B1
            (size_x, -size_y, -size_z),#B2

            ### left side face
            (-size_x, size_y, size_z),#4
            (-size_x, -size_y, size_z),#1
            (-size_x, -size_y, -size_z),#B1
            (-size_x, size_y, size_z),#4
            (-size_x, size_y, -size_z),#B4
            (-size_x, -size_y, -size_z),#B1
            ### right side face
            (size_x, size_y, size_z),#3
            (size_x, -size_y, size_z),#2
            (size_x, -size_y, -size_z),#B2
            (size_x, size_y, size_z),#3
            (size_x, size_y, -size_z),#B3
            (size_x, -size_y, -size_z),#B2

            ],
            None,
            [
            ### back face
            (0.0, ty_min),
            (1.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_max),
            
            ### front face
            (0.0, ty_min),
            (1.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_max),

            ### top face
            (0.0, ty_min),
            (1.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_max),

            ### bottom face
            (0.0, ty_min),
            (1.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_max),

            ### left side
            (0.0, ty_min),
            (1.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_max),
            ### right side 
            (0.0, ty_min),
            (1.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_max),
            ]
        )

