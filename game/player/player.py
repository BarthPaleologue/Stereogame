from feather.algebra import rotate
from feather.transform import Transform
from game.player.eye import Eye
from pygame.math import Vector3

class Player(Transform):
    
    def __init__(self, gamepad) :
        Transform.__init__(self)
        self.batte = None ### Initialiser la batte ici
        
        self.eyeDistance = 0.008

        self.oeilGauche = Eye() ### Initialiser l'oeil gauche ici
        self.oeilGauche.setPosition(-self.eyeDistance / 2, 0, 0)

        self.oeilDroit = Eye() ### Initialiser l'oeil droit ici
        self.oeilDroit.setPosition(self.eyeDistance / 2, 0, 0)

        self.gamepad = gamepad
        self.invincible = False
        self.state = 0
    
    def setinvincible(self, invincible) :
        self.invincible = invincible
    
    def reverseView(self) :
        self.oeilDroit, self.oeilGauche = self.oeilGauche, self.oeilDroit

    #def setFOV(self, fov):
    #    self.oeilDroit.fov = fov
    #    self.oeilGauche.fov = fov

    def setRotationX(self, angle):
        
        self.oeilDroit.setPosition(-self.eyeDistance / 2, 0, 0)
        self.oeilDroit.setRotationX(angle)
        self.oeilDroit.setRotationXAround(angle, self.position[0], self.position[1], self.position[2])
        self.oeilDroit.computeViewMatrix()

        self.oeilGauche.setPosition(self.eyeDistance / 2, 0, 0)
        self.oeilGauche.setRotationX(angle)
        self.oeilGauche.setRotationXAround(angle, self.position[0], self.position[1], self.position[2])
        self.oeilGauche.computeViewMatrix()

        super().setRotationX(angle)

    def setRotationY(self, angle):
        self.oeilDroit.setPosition(-self.eyeDistance / 2, 0, 0)
        self.oeilDroit.setRotationY(angle)
        self.oeilDroit.setRotationYAround(angle, self.position[0], self.position[1], self.position[2])
        self.oeilDroit.computeViewMatrix()

        self.oeilGauche.setPosition(self.eyeDistance / 2, 0, 0)
        self.oeilGauche.setRotationY(angle)
        self.oeilGauche.setRotationYAround(angle, self.position[0], self.position[1], self.position[2])
        self.oeilGauche.computeViewMatrix()
        
        super().setRotationY(angle)

    def setRotationZ(self, angle):
        self.oeilDroit.setPosition(-self.eyeDistance / 2, 0, 0)
        self.oeilDroit.setRotationZ(angle)
        self.oeilDroit.setRotationZAround(angle, self.position[0], self.position[1], self.position[2])
        self.oeilDroit.computeViewMatrix()

        self.oeilGauche.setPosition(self.eyeDistance / 2, 0, 0)
        self.oeilGauche.setRotationZ(angle)
        self.oeilGauche.setRotationZAround(angle, self.position[0], self.position[1], self.position[2])
        self.oeilGauche.computeViewMatrix()
        
        super().setRotationZ(angle)

    def setPosition(self, x, y, z):
        self.oeilDroit.setPosition(x - self.eyeDistance / 2, y, z)
        self.oeilGauche.setPosition(x + self.eyeDistance / 2, y, z)
        return super().setPosition(x, y, z)