from feather.shapes import Shape

class Ball(Shape):
        def __init__(self, name, position, velocity, acceleration ,trajectory, scene, flip = None):
            Shape.__init__(self, name, scene)
            ty_min = 0.0
            ty_max = 1.0
            if flip == True:
                ty_min = 1.0
                ty_max = 0.0

        def update(self):
            self.translate(self.position[0]+self.velocity[0], self.position[1]+self.velocity[1], self.position[2]+self.velocity[2])
            newVelocity = [self.velocity[0]+self.acceleration[0], self.velocity[1]+self.acceleration[1], self.velocity[2]+self.acceleration[2]]
            self.velocity = newVelocity


            
        


