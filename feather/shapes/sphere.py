from feather.shapes.shape import Shape
from math import sqrt
r = 1/20
class Sphere(Shape):
    def __init__(self, name, flip, scene = None):
        Shape.__init__(self, name, scene)
        ty_min = 0.0
        ty_max = 1.0
        if flip == True:
            ty_min = 1.0
            ty_max = 0.0

        self.build_buffers(
            [
            ### back face
            (0,0,-1),
            ( -r, r, -r),
            ( r, r, -r),
            (0,0,-1),
            ( r, r, -r),
            ( r, -r, -r),
            (0,0,-1),
            ( -r, -r, -r),
            ( r, -r, -r),
            (0,0,-1),
            (-r,-r,-r),
            (-r,r,-r),

            ### front face
            (0,0,1),
            ( -r, -r, r),
            ( -r, r, r),
            (0,0,1),
            ( -r, r, r),
            ( r, r, r),
            (0,0,1),
            ( r, r, r),
            ( r, -r, r),
            (0,0,1),
            (r,-r,r),
            (-r,-r,r),

            ### top face
            (0,1,0),
            (-r, r, r),
            (r, r, r),
            (0,1,0),
            (r, r, r),
            (r, r,-r),
            (0,1,0),
            (r, r, -r),
            (-r, r,-r),
            (0,1,0),
            (-r, r, -r),
            (-r, r, r),

            ### bottom face
            (0,-1,0),
            (-r, -r, r),
            (r, -r, r),
            (0,-1,0),
            (r, -r, r),
            (r, -r,-r),
            (0,-1,0),
            (r, -r, -r),
            (-r, -r,-r),
            (0,-1,0),
            (-r, -r, -r),
            (-r, -r, r),

            ### right face
            (1,0,0),
            (r, r, r),
            (r, r,-r),
            (1,0,0),
            (r, r, -r),
            (r, -r,-r),
            (1,0,0),
            (r, -r, -r),
            (r, -r,r),
            (1,0,0),
            (r, -r, r),
            (r, r, r),

            ### left face
            (-1,0,0),
            (-r, r, r),
            (-r, r,-r),
            (-1,0,0),
            (-r, r, -r),
            (-r, -r,-r),
            (-1,0,0),
            (-r, -r, -r),
            (-r, -r,r),
            (-1,0,0),
            (-r, -r, r),
            (-r, r, r),
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
            (0.0, ty_min),
            (1.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_max),

            ### right face
            (0.0, ty_min),
            (1.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_max),

            ### left face
            (0.0, ty_min),
            (1.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_min),
            (1.0, ty_max),
            (0.0, ty_max),
            ]
        )