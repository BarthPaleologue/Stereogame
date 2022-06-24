from game.eye import Eye

class Player :
    
    def __init__(self, position, perspective_mx, gamepad):
        self.position = position
        self.angleVision = perspective_mx
        self.batte = None ### Initialiser la batte ici
        self.oeilGauche = None ### Initialiser l'oeil gauche ici
        self.oeilDroit = None ### Initialiser l'oeil droit ici
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
    
    def reverseView(self) :
        self.oeilDroit, self.oeilGauche = self.oeilGauche, self.oeilDroit