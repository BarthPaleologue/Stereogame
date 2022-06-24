class Player :
    
    def __init__(self, position, angleVision, batte, oeilGauche, oeilDroit, gamepad, invincible, state) :
        self.position = position
        self.angleVision = angleVision
        self.batte = batte
        self.oeilGauche = oeilGauche
        self.oeilDroit = oeilDroit
        self.gamepad = gamepad
        self.invincible = invincible
        #self.state = state

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