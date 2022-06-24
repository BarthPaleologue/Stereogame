from geometry import *
class Battlefield(Shape):

    def __init__(self, name, size_x, size_y, size_z, flip = False):
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
            None, #1=0, 2=1, 3=2, 4= 4, B1 = 6, B2=7 , B3=8 , B4=10
            [
            ### back face
            (6,7),
            (6,8),
            (6,10),
            (8,7),
            (8,10),
            (8,6),
            
            ### front face
            (0,1),
            (0,2),
            (0,4),
            (2,0),
            (2,1),
            (2,4),

            ### top face
            (4,2),
            (2,8),
            (4,8),
            (4,10),
            (10,8),
            (4,8),

            ### bottom face
            (0,1),
            (1,7),
            (0,7),
            (0,6),
            (6,7),
            (0,7),

            ### left side
            (0,6),
            (0,10),
            (0,4),
            (10,6),
            (10,4),
            (10,0),
            ### right side 
            (1,7),
            (1,8),
            (1,3),
            (8,2),
            (8,7),
            (8,1),
            ]
        )

