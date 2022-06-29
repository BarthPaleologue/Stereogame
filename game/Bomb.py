from os import path
from game.projectile import Projectile
from feather.texture import *
from feather.materials import *
from feather.shapes.rectangle import Rectangle
import pygame
r = 1



class Bomb(Projectile):

    def __init__(self, name, flip, radius, battlefield, collision, scene):
        Projectile.__init__(self, name, flip, radius, battlefield, collision, scene)
        self.scene = scene
        bombMat = TextureMaterial(Texture("./assets/explosion.png"))
        self.setMaterial(bombMat)

    def explode(self):
        crash_sound = pygame.mixer.Sound("./assets/explosion1.wav")
        pygame.mixer.Sound.play(crash_sound)
        pygame.mixer.music.stop()
        self.destroy()
        
        """explosion_anim = {}
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
            #rect.setScaling(0,0,0)"""

        
        
        

