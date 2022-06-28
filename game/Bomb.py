from os import path
from game.ball import Ball
from feather.texture import *
from feather.materials import *
from feather.shapes.rectangle import Rectangle
import pygame
r = 1



class Bomb(Ball):

    def __init__(self, name, flip, radius, scene):
        Ball.__init__(self,name, flip, radius, scene)
        self.scene = scene

    def explode(self):
        position = self.getPosition()
        bombMat = TextureMaterial(Texture("./assets/explosion.png"))
        self.setMaterial(bombMat)
        #crash_sound = pygame.mixer.Sound("./assets/explosion1.wav")
        #pygame.mixer.Sound.play(crash_sound)
        #pygame.mixer.music.stop()
        explosion_anim = {}
        explosion_anim['lg'] = []
        explosion_anim['sm'] = []
        for i in range(9):
            filename = './assets/regularExplosion0{}.png'.format(i)
            rect = Rectangle("recty",True,self.scene)
            rect.setPosition(position[0],position[1],position[2])
            imagMat = TextureMaterial(Texture(filename))
            rect.setMaterial(imagMat)
            rect.setScaling(1.5,1.5,1.5)
            pygame.time.delay(2)
            #rect.setScaling(0,0,0)

        
        """self.setScene=None
        velocity = self.getVelocity()
        self.setVelocity(velocity[0]*r, velocity[1]*r, velocity[2]*r) 
        bombMat = TextureMaterial(Texture("./assets/explosion.png"))
        self.setMaterial(bombMat)
        crash_sound = pygame.mixer.Sound("./assets/explosion1.wav")
        pygame.mixer.Sound.play(crash_sound)
        pygame.mixer.music.stop()"""
        
        
        
