from locale import normalize
import math
import numpy as np

#creates a rotation matrix of angle (in degrees) around axis vec3(x,y,z)
def rotate(angle, x, y, z):
    s = math.sin(math.radians(angle))
    c = math.cos(math.radians(angle))
    magnitude = math.sqrt(x*x + y*y + z*z)
    nc = 1 - c
      
    x /= magnitude
    y /= magnitude
    z /= magnitude

    return np.array([
        [     c + x**2 * nc, y * x * nc - z * s, z * x * nc + y * s, 0],
        [y * x * nc + z * s,      c + y**2 * nc, y * z * nc - x * s, 0],
        [z * x * nc - y * s, z * y * nc + x * s,      c + z**2 * nc, 0],
        [                 0,                  0,                  0, 1],
    ])

#creates a translation matrix of vec3(x,y,z)
def translate(x, y, z):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [x, y, z, 1],
    ])

#creates a scale matrix
def scale(x, y, z):
    return np.array([
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1],
    ])
def reflection(vec, normal):
    for i in range(3):
        vec[i]=-vec[i]
    ps = (vec[0]*normal[0] + vec[1]*normal[1] + vec[2]*normal[2])
    # return 2*ps*normal - vec
    res = [0,0,0]
    for i in range(3):
        res[i]=2*ps*normal[i] - vec[i]
    return res

print(reflection([-1,-1,-1],[0,1,0]))

