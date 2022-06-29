from feather.materials.textureMaterial import TextureMaterial
from feather.shapes import Sphere, Rectangle
from feather.algebra import reflection
import numpy as np
import pygame
from random import random

from feather.texture import Texture
from feather.vector3 import Vec3

class Projectile(Sphere):
        def __init__(self, name, flip,  radius, battlefield, collision, ballmanager, scene):
            Sphere.__init__(self, name, flip, scene)
            self.collision = collision  # if it is equal to reflect, then it will reflect
                                        # and if it is equal to teleport than we will apply the function teleport
            self.position = Vec3(0.0, 0.0, 0.0)
            self.velocity = Vec3(0.0, 0.0, 0.0)
            self.acceleration = Vec3(0.0, 0.0, 0.0)
            self.radius = radius
            self.battlefield = battlefield
            self.ballmanager = ballmanager
            self.setScaling(radius, radius, radius)

            self.currentPlayer = None


        def update(self):
            r = self.getRadius()
            position = self.getPosition()
            x,y,z = position.x, position.y, position.z
            sizex,sizey,sizez = self.battlefield.getSizex(), self.battlefield.getSizey(), self.battlefield.getSizez()
            if self.battlefield.isCollision(r, position):
                where = self.battlefield.whereCollision(r, position)
                if self.collision == 'reflect':
                    normVect = self.battlefield.normalVector(where)
                    oldVelocity = self.getVelocity()
                    newVelocity = reflection(oldVelocity, normVect)

                    self.setVelocity(newVelocity.x, newVelocity.y, newVelocity.z)
                if self.collision == 'teleport':
                    
                    if where == 'right':
                        self.setPosition(x-2*sizex+2*r + 0.1, y, z)
                    elif where == 'left':
                        self.setPosition(x+2*sizex-2*r-0.1, y, z)
                    elif where == 'top':
                        self.setPosition(x, y - 2*sizey + 2*r - 0.1, z)
                    elif where == 'bottom':
                        self.setPosition(x, y + 2*sizey - 2*r + 0.1, z)
                if self.collision == 'bomb':
                    self.explode()


            self.translate(self.velocity.x, self.velocity.y, self.velocity.z)
            newVelocity = Vec3(self.velocity.x+self.acceleration.x, self.velocity.y+self.acceleration.y, self.velocity.z+self.acceleration.z)
            self.velocity = newVelocity
            
        def setVelocity(self, x, y, z):
           self.velocity = Vec3(x, y, z)

        def getVelocity(self):
            return self.velocity

        def setAcceleration(self, x, y, z):
            self.acceleration = Vec3(x, y, z)

        def getAcceleration(self):
            return self.acceleration

        def getRadius(self):
            return self.radius

        def getEnds(self):
            futurePosition = np.array([self.position.x+self.velocity.x, self.position.y+self.velocity.y, self.position.z+self.velocity.z])
            ends = np.add(self.vertices, np.full((len(self.vertices), 3), futurePosition))
            return ends

        def setCollision(self, collision):
            self.collision = collision
        
        def showTrajectory(self):
            traj = Rectangle('traj', False, self.scene)
            traj.setPosition(self.position.x, self.position.y, self.position.z)
            traj.setScaling(0.5, 0.005, 1)

        def applyEffect(self, effect):
            if effect == 'disparition':
                ballMat = TextureMaterial(Texture("./assets/texBattle.jpeg"))
                self.setMaterial(ballMat)
                #self.update()
            elif effect == 'teleport':
                ballMat = TextureMaterial(Texture("./assets/Galaxy512.jpg"))
                self.setMaterial(ballMat)
                self.setCollision('teleport')
                #self.update()
            elif effect == 'bomb':
                self.setCollision('bomb')
                bombMat = TextureMaterial(Texture("./assets/explosion.png"))
                self.setMaterial(bombMat)
                #self.update()
            elif effect == 'x3':
                position = self.getPosition()
                x,y,z = position.x, position.y, position.z
                proj1 = Projectile("sphery", False, 1, self.battlefield, 'reflect',self.ballmanager, self.scene)
                proj2 = Projectile("sphery", False, 1, self.battlefield, 'reflect',self.ballmanager, self.scene)
                ballMat = TextureMaterial(Texture("./assets/basketball.jpeg"))
                proj1.setMaterial(ballMat)
                proj2.setMaterial(ballMat)
                proj1.setPosition(x,y,z)
                proj2.setPosition(x,y,z)
                proj1.setVelocity((random() - 0.5) / 2.0, (random() - 0.5) / 2.0, (random() - 0.5) / 2.0)
                proj2.setVelocity((random() - 0.5) / 2.0, (random() - 0.5) / 2.0, (random() - 0.5) / 2.0)
                proj1.ballmanager.addBall(proj1)
                proj2.ballmanager.addBall(proj2)
            elif effect == 'superbat':
                if self.currentPlayer != None:
                    self.currentPlayer.batte.isSuperBat = True

        def explode(self):
            crash_sound = pygame.mixer.Sound("./assets/explosion1.wav")
            pygame.mixer.Sound.play(crash_sound)
            self.ballmanager.removeBall(self)