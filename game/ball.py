from feather.shapes import Sphere, Rectangle
import numpy as np

class Ball(Sphere):
        def __init__(self, name, flip,  radius, scene):

            Sphere.__init__(self, name, flip, radius, scene)
            self.position = np.array([0.0, 0.0, 0.0])
            self.velocity = np.array([0.0, 0.0, 0.0])
            self.acceleration = np.array([0.0, 0.0, 0.0])
            self.radius = radius


        def update(self):
            self.translate(self.velocity[0], self.velocity[1], self.velocity[2])
            newVelocity = np.array([self.velocity[0]+self.acceleration[0], self.velocity[1]+self.acceleration[1], self.velocity[2]+self.acceleration[2]])  
            self.velocity = newVelocity
            
        def setVelocity(self, x, y, z):
           self.velocity = np.array([x, y, z])

        def getVelocity(self):
            return self.velocity

        def setAcceleration(self, x, y, z):
            self.acceleration = np.array([x, y, z])

        def getAcceleration(self):
            return self.acceleration

        def getRadius(self):
            return self.radius

        def getEnds(self):
            futurePosition = np.array([self.position[0]+self.velocity[0], self.position[1]+self.velocity[1], self.position[2]+self.velocity[2]])
            ends = np.add(self.vertices, np.full((len(self.vertices), 3), futurePosition))
            return ends
        
        def showTrajectory(self):
            traj = Rectangle('traj', False, self.scene)
            traj.setPosition(self.position[0], self.position[1], self.position[2])
            traj.setScaling(0.5, 0.005, 1)

            
        


