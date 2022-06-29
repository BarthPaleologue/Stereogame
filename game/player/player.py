from feather.transform import Transform
from feather.collisions.sphereToCylinder import sphereToCylinder
from game.player.GamePad import GamePad
from game.player.eye import Eye
from pygame.math import Vector3
from game.bat import Bat


class Player(Transform):
    def __init__(self, flip, gamepad, scene, ballManager):
        Transform.__init__(self)
        self.batte = Bat("./assets/baseball/batB.obj", scene)

        self.eyeDistance = 0.0069

        self.leftEye = Eye()  ### Initialiser l'oeil gauche ici
        self.leftEye.setPosition(-self.eyeDistance / 2, 0, 0)

        self.rightEye = Eye()  ### Initialiser l'oeil droit ici
        self.rightEye.setPosition(self.eyeDistance / 2, 0, 0)

        if (flip):
            self.rightEye, self.leftEye = self.leftEye, self.rightEye

        self.flip = flip

        self.setEyesTarget(0, 0, 0)

        self.gamepad = gamepad
        self.invincible = False
        self.state = 0

        self.ballManager = ballManager
   
    def getGamepad(self) :
        return self.gamepad

    def setinvincible(self, invincible):
        self.invincible = invincible

    def reverseView(self):
        self.rightEye, self.leftEye = self.leftEye, self.rightEye

    # def setFOV(self, fov):
    #    self.oeilDroit.fov = fov
    #    self.oeilGauche.fov = fov

    def setRotationX(self, angle):

        self.rightEye.setPosition(-self.eyeDistance / 2, 0, 0)
        self.rightEye.setRotationX(angle)
        self.rightEye.setRotationXAround(angle, self.position[0], self.position[1], self.position[2])
        self.rightEye.computeViewMatrix()

        self.leftEye.setPosition(self.eyeDistance / 2, 0, 0)
        self.leftEye.setRotationX(angle)
        self.leftEye.setRotationXAround(angle, self.position[0], self.position[1], self.position[2])
        self.leftEye.computeViewMatrix()

        super().setRotationX(angle)

    def setRotationY(self, angle):
        self.rightEye.setPosition(-self.eyeDistance / 2, 0, 0)
        self.rightEye.setRotationY(angle)
        self.rightEye.setRotationYAround(angle, self.position[0], self.position[1], self.position[2])
        self.rightEye.computeViewMatrix()

        self.leftEye.setPosition(self.eyeDistance / 2, 0, 0)
        self.leftEye.setRotationY(angle)
        self.leftEye.setRotationYAround(angle, self.position[0], self.position[1], self.position[2])
        self.leftEye.computeViewMatrix()

        super().setRotationY(angle)

    def setRotationZ(self, angle):
        self.rightEye.setPosition(-self.eyeDistance / 2, 0, 0)
        self.rightEye.setRotationZ(angle)
        self.rightEye.setRotationZAround(angle, self.position[0], self.position[1], self.position[2])
        self.rightEye.computeViewMatrix()

        self.leftEye.setPosition(self.eyeDistance / 2, 0, 0)
        self.leftEye.setRotationZ(angle)
        self.leftEye.setRotationZAround(angle, self.position[0], self.position[1], self.position[2])
        self.leftEye.computeViewMatrix()

        super().setRotationZ(angle)

    def setPosition(self, x, y, z):
        self.rightEye.setPosition(x - self.eyeDistance / 2, y, z)
        self.leftEye.setPosition(x + self.eyeDistance / 2, y, z)
        self.batte.setPosition(x, y, z)
        if self.flip:
            self.batte.translate(0, 0, -0.5)
            self.batte.beginY = -30
            self.batte.beginZ = 50
            self.batte.endZ = 50
            self.batte.setRotationZ(self.batte.beginZ)
            self.batte.setRotationY(self.batte.beginY)
        else:
            self.batte.translate(0, 0, 0.5)
            self.batte.beginZ = 180 - 50
            self.batte.endZ = 180 - 50
            self.batte.beginY = 30
            self.batte.setRotationZ(self.batte.beginZ)
            self.batte.setRotationY(self.batte.beginY)

        return super().setPosition(x, y, z)

    def setEyesTarget(self, x, y, z):
        self.rightEye.setTarget(Vector3(x, y, z))
        self.leftEye.setTarget(Vector3(x, y, z))

    def setEyeDistance(self, eyeDistance):
        self.eyeDistance = eyeDistance
        self.rightEye.setPosition(self.position[0] - self.eyeDistance / 2, self.position[1], self.position[2])
        self.leftEye.setPosition(self.position[0] + self.eyeDistance / 2, self.position[1], self.position[2])

    def invertEyes(self):
        self.rightEye, self.leftEye = self.leftEye, self.rightEye

    def update(self, deltaTime: float):
        self.batte.update(deltaTime)
        for ball in self.ballManager.balls:
            if sphereToCylinder(ball, self.batte):
                print("!!!!")
                if self.flip:
                    ball.setVelocity(0, 0, -0.5)
                else:
                    ball.setVelocity(0, 0, 0.5)
