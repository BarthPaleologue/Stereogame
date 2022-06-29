from feather.materials.textureMaterial import TextureMaterial
from feather.shapes import Sphere, Rectangle
from feather.algebra import reflection
import numpy as np
import pygame

from feather.texture import Texture

class Projectile(Sphere):
        def __init__(self, name, flip,  radius, battlefield, collision, ballmanager, scene):
            Sphere.__init__(self, name, flip, scene)
            self.collision = collision  # if it is equal to reflect, then it will reflect
                                        # and if it is equal to teleport than we will apply the function teleport
            self.position = np.array([0.0, 0.0, 0.0])
            self.velocity = np.array([0.0, 0.0, 0.0])
            self.acceleration = np.array([0.0, 0.0, 0.0])
            self.radius = radius
            self.battlefield = battlefield
            self.ballmanager = ballmanager
            self.setScaling(radius, radius, radius)

            self.currentPlayer = None


        def update(self):
            r = self.getRadius()
            position = self.getPosition()
            x,y,z = position[0], position[1], position[2]
            sizex,sizey,sizez = self.battlefield.getSizex(), self.battlefield.getSizey(), self.battlefield.getSizez()
            if self.battlefield.isCollision(r, position):
                if self.collision == 'reflect':
                    normVect = self.battlefield.normalVector(self.battlefield.whereCollision(self.getRadius(), self.getPosition()))
                    oldVelocity = self.getVelocity()
                    newVelocity = reflection(oldVelocity, normVect)

                    self.setVelocity(newVelocity[0], newVelocity[1], newVelocity[2])
                if self.collision == 'teleport':
                    if self.battlefield.whereCollision(r, position) == 'right':
                        self.setPosition(x-2*sizex+2*r + 0.1, y, z)
                    elif self.battlefield.whereCollision(r, position) == 'left':
                        self.setPosition(x+2*sizex-2*r-0.1, y, z)
                    elif self.battlefield.whereCollision(r, position) == 'top':
                        self.setPosition(x, y - 2*sizey + 2*r - 0.1, z)
                    elif self.battlefield.whereCollision(r, position) == 'bottom':
                        self.setPosition(x, y + 2*sizey - 2*r + 0.1, z)
                if self.collision == 'bomb':
                    self.explode()


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

        def setCollision(self, collision):
            self.collision = collision
        
        def showTrajectory(self):
            traj = Rectangle('traj', False, self.scene)
            traj.setPosition(self.position[0], self.position[1], self.position[2])
            traj.setScaling(0.5, 0.005, 1)

        def applyEffect(self, effect):
            if effect == 'disparition':
                ballMat = TextureMaterial(Texture("./assets/texBattle.jpeg"))
                self.setMaterial(ballMat)
                self.update()
            elif effect == 'teleport':
                self.setCollision('teleport')
                self.update()
            elif effect == 'bomb':
                self.setCollision('bomb')
                bombMat = TextureMaterial(Texture("./assets/explosion.png"))
                self.setMaterial(bombMat)
                self.update()
        
        def explode(self):
            crash_sound = pygame.mixer.Sound("./assets/explosion1.wav")
            pygame.mixer.Sound.play(crash_sound)
            self.ballmanager.removeBall(self)