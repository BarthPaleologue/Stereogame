from feather.shapes import Sphere, Rectangle

class Ball(Sphere):
        def __init__(self, name, position, velocity, acceleration,  scene, flip = None):

            Sphere.__init__(self, name, scene)
            self.position = position
            self.velocity = velocity
            self.acceleration = acceleration
            
            ty_min = 0.0
            ty_max = 1.0
            if flip == True:
                ty_min = 1.0
                ty_max = 0.0

        def update(self):
            self.translate(self.position[0]+self.velocity[0], self.position[1]+self.velocity[1], self.position[2]+self.velocity[2])
            newVelocity = [self.velocity[0]+self.acceleration[0], self.velocity[1]+self.acceleration[1], self.velocity[2]+self.acceleration[2]]
            self.velocity = newVelocity

        def getVelocity(self):
            return self.velocity

        def getAcceleration(self):
            return self.acceleration

        def showTrajectory(self):
            #creer rectangle fin + prend position initiale position balle 
            #rotate le rectangle selon velocity + tracer uniquement une partie de la trajectoire
            traj = Rectangle('traj', False, self.scene)
            traj.setPosition(self.position[0], self.position[1], self.position[2])
            traj.setScaling(0.5, 0.005, 1)
            traj.setRotationY(45)



            
        


