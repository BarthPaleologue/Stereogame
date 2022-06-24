from game.player.eye import Eye
from pygame.math import Vector3

class Player :
    
    def __init__(self, position, perspective_mx, gamepad, eye_target) :
        self.position = position
        self.angleVision = perspective_mx
        self.eye_target = eye_target
        self.batte = None ### Initialiser la batte ici
        self.oeilGauche = Eye((position[0] + 0.008/2.0, 0, 5), eye_target) ### Initialiser l'oeil gauche ici
        self.oeilDroit = Eye((position[0] - 0.008/2.0, 0, 5), eye_target) ### Initialiser l'oeil droit ici
        self.gamepad = gamepad
        self.invincible = False
        self.state = 0

    def getPosition(self) :
        return self.position

    def getAngleVision(self) :
        return self.angleVision
    
    def getBatte(self) :
        return self.batte
    
    def getOeilGauche(self) :
        return self.oeilGauche
    
    def getOeilDroit(self) :
        return self.oeilDroit
    
    def getGamepad(self) :
        return self.gamepad
    
    def setinvincible(self) :
        if self.invincible :
            self.invincible = False
        else :
            self.invincible = True
    
    def getEye_Target(self) :
        return self.eye_target
    
    def reverseView(self) :
        self.oeilDroit, self.oeilGauche = self.oeilGauche, self.oeilDroit