class Player :
    
    def __init__(self, position, angleVision, batte, oeilGauche, oeilDroit, gamepad) :
        self.position = position
        self.angleVision = angleVision
        self.batte = batte
        self.oeilGauche = oeilGauche
        self.oeilDroit = oeilDroit
        self.gamepad = gamepad

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
    
    def reverseView(self) :
        self.oeilDroit, self.oeilGauche = self.oeilGauche, self.oeilDroit