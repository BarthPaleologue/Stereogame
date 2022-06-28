from feather.shapes import Sphere, Rectangle
from feather.algebra import reflection
import numpy as np

class Projectile(Sphere):
        def __init__(self, name, flip,  radius, battlefield, scene):

            Sphere.__init__(self, name, flip, scene)
            self.position = np.array([0.0, 0.0, 0.0])
            self.velocity = np.array([0.0, 0.0, 0.0])
            self.acceleration = np.array([0.0, 0.0, 0.0])
            self.radius = radius
            self.battlefield = battlefield

            self.setScaling(radius, radius, radius)


        def update(self):
            if self.battlefield.isCollision(self.getRadius(), self.getPosition()):
                normVect = self.battlefield.normalVector(self.battlefield.whereCollision(self.getRadius(), self.getPosition()))
                oldVelocity = self.getVelocity()
                newVelocity = reflection(oldVelocity, normVect)

                self.setVelocity(newVelocity[0], newVelocity[1], newVelocity[2])

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

            
        


