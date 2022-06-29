from random import random
from OpenGL.GL import *
import numpy as np
from game.projectile import Projectile

from game.BallManager import BallManager
from game.MysteryBox import MysteryBox
from game.Bomb import Bomb
from game.player.GamePad import GamePad
from game.player.Keyboard import Keyboard
import pygame

#local imports
from feather import Texture, Scene, Screen
from feather.shapes import Rectangle, Cube
from feather.materials import ColorMaterial, TextureMaterial, ShaderMaterial
from feather.projections import *
from feather.algebra import *
from feather.camera import *
from interlacer import Interlacer
from feather.loaders.RowOBJ import RowOBJ
from game import Player, Battlefield, Projectile

def drawEyeToFrameBuffer(eye, scene, testMat, testTexture):
    eye.frameBuffer.bind()
    glViewport(0, 0, eye.frameBuffer.width, eye.frameBuffer.height)

    testMat.texture = testTexture

    scene.render(eye.getProjectionMatrix(), model_matrix, eye.computeViewMatrix())

if __name__ == "__main__":
    pygame.init()
    width, height = 1920, 1080
    #infoObject = pygame.display.Info()
    #width, height = infoObject.current_w, infoObject.current_h
    pygame.display.set_mode((width, height), pygame.DOUBLEBUF|pygame.OPENGL|pygame.HWSURFACE, 0)
    pygame.display.toggle_fullscreen()

    scene = Scene()

    DOES_INTERLACE = False
    
    ######## DECLARATION DES SHAPES

    battlefield = Battlefield("battly", 10, 6, 18, scene)
    battleMat2 = ShaderMaterial("./game/battlefieldMat/vertex.glsl", "./game/battlefieldMat/fragment.glsl")
    battlefield.setMaterial(battleMat2)

    sphereTex = Texture("./assets/space.png")

    ballManager = BallManager([])
    mysteryBox = MysteryBox("boxy", battlefield, scene)
    for i in range(8):
        sphere = Projectile("sphery", False, 1, battlefield, 'reflect',ballManager, scene)
        sphere.setPosition(-2, 0, 0)
        sphere.setVelocity((random() - 0.5) / 2.0, (random() - 0.5) / 2.0, (random() - 0.5) / 2.0)
        sphereMat = TextureMaterial(sphereTex)
        sphere.setMaterial(sphereMat)
        ballManager.addBall(sphere)
    
    rect = Rectangle('rect', True, scene)
    rect.setPosition(-5, 0, 0).setScaling(0.5, 0.5, 1)

    rectMat = TextureMaterial(Texture("./assets/black.jpg"))
    rect.setMaterial(rectMat)

    yellow_cube = Cube('yellow_cube', True, scene)
    yellow_cube.setRotationY(45)
    
    cubeMat = TextureMaterial(Texture("./assets/tennis.png"))
    yellow_cube.setMaterial(cubeMat)

    blackTex = Texture("./assets/black.jpg")
    numTextures = [Texture(f"./assets/numbers/{i}.png") for i in range(8)]
    
    ######### DECLARATION DE L'ECRAN

    screen = Screen('screen')

    ######### MATRICES UTILES

    perspective_mx = perspective(45, width / height, 0.1, 100)
    model_matrix = np.identity(4, dtype=np.float32)
    ortho_mx = ortho(-1, 1, 1, -1, -50, 50)
    ident_matrix = np.identity(4, dtype=np.float32)

    ######### DECLARATION DES JOUEURS

    keyboard = Keyboard()
    nb_joystick = pygame.joystick.get_count()
    pygame.joystick.init()
    if nb_joystick > 0 :
        joystick = []
        gamepad = []
        for i in range (nb_joystick) :
            joystick += [pygame.joystick.Joystick(i)]
            gamepad += [GamePad(i)]
        player1 = Player(False, gamepad[0], scene, ballManager)
        if nb_joystick == 2 :
            player2 = Player(True, gamepad[1], scene, ballManager)
        else :
            player2 = Player(False, None, scene, ballManager)
    else :
        player1 = Player(False, None, scene, ballManager)
        player2 = Player(True, None, scene, ballManager)

    player1.setPosition(0, 0, -12)
    player2.setPosition(0, 0, 12)

    end1 = Cube("end1", False, scene)

    fbo_width = int(width/2)
    fbo_height = int(height/2)

    ######### DECLARATION DE L'ENTRELACEUR

    interlacer = Interlacer()

    ######### DECLARATION DES VARIABLES DE LA BOUCLE

    getTicksLastFrame = 0.0
    x,z = 0.0, 0.0
    circleRadius = 2.5

    ######### GAME LOOP
    
    running = True
    while running:
        time = pygame.time.get_ticks() / 1000.0
        deltaTime = time - getTicksLastFrame
        getTicksLastFrame = time

        ###### UPDATE ETAT DES SHAPES

        player1.update(deltaTime)
        player2.update(deltaTime)
        
        yellow_cube.addRotationY(deltaTime * 70.0).addRotationX(deltaTime * 80.0)

        rotationSpeed = 1
        x = math.cos(time * rotationSpeed) * circleRadius
        z = math.sin(time * rotationSpeed) * circleRadius

        yellow_cube.setPosition(x, 0, z)

        end1.setPosition(player1.batte.end1[0], player1.batte.end1[1], player1.batte.end1[2] - 4.5)

        for sphere in ballManager.balls:
            sphere.update()
            sphere.setRotationY(time * 50.0)
            sphere.setRotationX(time * 60.0)
            sphere.setRotationZ(time * 40.0)
            if mysteryBox.isCollision(sphere):
                mysteryBox.onHit(sphere)

            
        """for bomb in spheres:
            if battlefield.isCollision(bomb.getRadius(), bomb.getPosition()):
                bomb.explode()
            bomb.update()
            bomb.setRotationY(time * 50.0)
            bomb.setRotationX(time * 60.0)
            bomb.setRotationZ(time * 40.0)"""
            


        ###### DESSIN DES SHAPES SUR FRAMEBUFFER

        ### PLAYER 1
        drawEyeToFrameBuffer(player1.rightEye, scene, rectMat, numTextures[1])
        drawEyeToFrameBuffer(player1.leftEye, scene, rectMat, numTextures[2])

        ### PLAYER 2
        drawEyeToFrameBuffer(player2.rightEye, scene, rectMat, numTextures[5])
        drawEyeToFrameBuffer(player2.leftEye, scene, rectMat, numTextures[6])
        

        ###### DESSIN DES FRAMEBUFFER SUR L'ECRAN

        glUseProgram(0)
        #render to main video output
        glBindFramebuffer(GL_FRAMEBUFFER, 0)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_BLEND)

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glViewport(0, 0, width, height)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        ###### ENTRELACEMENT DES FRAMEBUFFERS

        interlacer.use(ortho_mx, ident_matrix)

        if DOES_INTERLACE:

            interlacer.setTextureFromFBO(player1.rightEye.frameBuffer, 1)
            interlacer.setTextureFromFBO(player1.leftEye.frameBuffer, 2)
            #interlacer.setTextureFromImage(blackTex, 0)
            #interlacer.setTextureFromImage(blackTex, 1)

            interlacer.setTextureFromImage(blackTex, 3)
            interlacer.setTextureFromImage(blackTex, 4)
            
            interlacer.setTextureFromFBO(player2.rightEye.frameBuffer, 5)
            interlacer.setTextureFromFBO(player2.leftEye.frameBuffer, 6)
            #interlacer.setTextureFromImage(blackTex, 4)
            #interlacer.setTextureFromImage(blackTex, 5)

            interlacer.setTextureFromImage(blackTex, 7)
            interlacer.setTextureFromImage(blackTex, 0)

        else:
            interlacer.setTextureFromFBO(player1.rightEye.frameBuffer, 0)
            interlacer.setTextureFromFBO(player1.rightEye.frameBuffer, 1)
            interlacer.setTextureFromFBO(player1.rightEye.frameBuffer, 2)
            interlacer.setTextureFromFBO(player1.rightEye.frameBuffer, 3)
            interlacer.setTextureFromFBO(player1.rightEye.frameBuffer, 4)
            interlacer.setTextureFromFBO(player1.rightEye.frameBuffer, 5)
            interlacer.setTextureFromFBO(player1.rightEye.frameBuffer, 6)
            interlacer.setTextureFromFBO(player1.rightEye.frameBuffer, 7)

        screen.draw(interlacer.program)

        pygame.display.flip()

        ####### GESTION DES ENTREES CLAVIER

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            circleRadius += 0.05
        if keys[pygame.K_s]:
            circleRadius -= 0.05
        if keys[pygame.K_q]:
            player1.setEyeDistance(player1.eyeDistance + 0.001)
            player2.setEyeDistance(player2.eyeDistance + 0.001)
        if keys[pygame.K_d]:
            player1.setEyeDistance(player1.eyeDistance - 0.001)
            player2.setEyeDistance(player2.eyeDistance - 0.001)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if player1.getGamepad() == None :
                    player1.batte.strike()
                if player2.getGamepad() == None :
                    player2.batte.strike()
            if event.type == pygame.MOUSEMOTION:
                x, y = event.rel
                if any(event.buttons):
                    model_matrix = model_matrix.dot(rotate(y, -1, 0, 0)).dot(rotate(x, 0, -1, 0))
            # pour tester si le programme detecte les appuie sur les boutons
            if event.type == pygame.JOYBUTTONDOWN:
                if nb_joystick > 0 :
                    for i in range (nb_joystick) :
                        gamepad[i].update()
                        if gamepad[i].isBattePressed():
                            print(i)
                if player1.getGamepad() != None and player1.getGamepad().isBattePressed() == 0 :
                    player1.batte.strike()
                if player2.getGamepad() != None and player2.getGamepad().isBattePressed() == 0 :
                    player2.batte.strike()
        '''
        keyboard.update()
        if keyboard.isBattePressed():
            print("batty")
        if nb_joystick > 0 :
            for i in range (nb_joystick) :
                gamepad[i].update()
                if gamepad[i].isBattePressed():
                    print("joybatty")'''