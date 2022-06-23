import numpy as np
from OpenGL.GL import *
import math
import pygame
from feather.algebra import *


#creates a perspective projection matrix
# - fovy: field of view along vertical axis
# - aspect: aspect ratio (width/height)
# - z_near: z coord of near z clipping plane
# - z_far: z coord of far z clipping plane
def perspective(fovy, aspect, z_near, z_far):
    f = 1 / math.tan(math.radians(fovy) / 2)
    return np.array([
        [f / aspect,  0,                                   0,  0],
        [          0, f,                                   0,  0],
        [          0, 0, (z_far + z_near) / (z_near - z_far), -1],
        [          0, 0, (2*z_far*z_near) / (z_near - z_far),  0]
    ])


#creates an orthogonal perspective projection matrix
def ortho(left, right, top, bottom, z_near, z_far):
    m11 = 2 / (right-left);
    m22 = 2 / (top-bottom);
    m33 = -2 / (z_far-z_near);
    m34 = (right+left) / (right-left);
    m42 = (top+bottom) / (top-bottom);
    m43 = (z_far+z_near) / (z_far-z_near);
    return np.array([
        [m11, 0, 0,  0],
        [0, m22, 0,  0],
        [0, 0, m33, m34],
        [0, m42, m43, 1]
    ])

#creates a lookat view matrix looking at center from eye with up-vector equal to Y axis
def lookat(eye, center):
    zaxis = center - eye
    zaxis = zaxis.normalize()
    up = pygame.math.Vector3(0, 1, 0)

    xaxis = zaxis.cross(up).normalize()
    yaxis = xaxis.cross(zaxis).normalize()
    zaxis = -zaxis

    return np.array([
        [xaxis.x, xaxis.y, xaxis.z, -xaxis.dot(eye)],
        [yaxis.x, yaxis.y, yaxis.z, -yaxis.dot(eye)],
        [zaxis.x, zaxis.y, zaxis.z, -zaxis.dot(eye)],
        [0, 0, 0, 1]
    ]).transpose().dot(scale(1, -1, 1))



