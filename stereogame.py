from random import random
from OpenGL.GL import *
import numpy as np

from feather.textTexture import TextTexture
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

def drawEyeToFrameBuffer(eye, scene, testMat, testTexture, scoreTexture):
    eye.frameBuffer.bind()
    glViewport(0, 0, eye.frameBuffer.width, eye.frameBuffer.height)

    #testMat.texture = testTexture
    testMat.texture = scoreTexture

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

    ####### BALL MANAGER
    ballManager = BallManager([])

    ######### DECLARATION DES JOUEURS

    keyboard = Keyboard()
    nb_joystick = pygame.joystick.get_count()
    pygame.joystick.init()
    if nb_joystick > 0 :
        joystick = []
        gamepad = []
        for i in range (nb_joystick) :
            #joystick += [pygame.joystick.Joystick(i)]
            #gamepad += [GamePad(i)]
            joystick.append(pygame.joystick.Joystick(i))
            gamepad.append(GamePad(i))
        player1 = Player(False, gamepad[0], scene, ballManager)
        if nb_joystick == 2:
            player2 = Player(True, gamepad[1], scene, ballManager)
        else:
            player2 = Player(False, None, scene, ballManager)
    else:
        player1 = Player(False, None, scene, ballManager)
        player2 = Player(True, None, scene, ballManager)

    player1.setPosition(0, 0, -21.2)
    player2.setPosition(0, 0, 21.2)
    
    ######## DECLARATION DES SHAPES

    battlefield = Battlefield("battly", 10, 6, 30, player1, player2, scene)
    battleMat2 = ShaderMaterial("./game/battlefieldMat/vertex.glsl", "./game/battlefieldMat/fragment.glsl")
    battlefield.setMaterial(battleMat2)

    sphereTex = Texture("./assets/normaltex.jpeg")

    mysteryBoxes = []
    for i in range(3):
        mysteryBox = MysteryBox("boxy", battlefield, scene)
        mysteryBoxes.append(mysteryBox)

    sphere = Projectile("sphery", False, 1, battlefield, 'reflect', ballManager, scene)
    sphere.setPosition(0, 1, 0)
    sphere.setVelocity((random() - 0.5) / 2, (random() - 0.5) / 2, (random() - 0.5))
    sphereMat = TextureMaterial(sphereTex)
    sphere.setMaterial(sphereMat)
    
    rect = Rectangle('rect', False, scene)
    rect.setPosition(-4, 2, -3).setScaling(1, 1, 1)

    rectMat = TextureMaterial(Texture("./assets/black.jpg"))
    rect.setMaterial(rectMat)

    blackTex = Texture("./assets/black.jpg")
    numTextures = [TextTexture(f"{i}", (0, 0, 0), (255, 255, 255)) for i in range(8)]
    
    ######### DECLARATION DE L'ECRAN

    screen = Screen('screen')

    ######### MATRICES UTILES

    perspective_mx = perspective(45, width / height, 0.1, 100)
    model_matrix = np.identity(4, dtype=np.float32)
    ortho_mx = ortho(-1, 1, 1, -1, -50, 50)
    ident_matrix = np.identity(4, dtype=np.float32)

    #end1 = Cube("end1", False, scene)

    fbo_width = int(width/2)
    fbo_height = int(height/2)

    ######### DECLARATION DE L'ENTRELACEUR

    interlacer = Interlacer()

    ######### DECLARATION DES VARIABLES DE LA BOUCLE

    getTicksLastFrame = 0.0

    ######### GAME LOOP
    
    running = True
    service = True
    
    score1 = 0
    score2 = 0
    while running:
        time = pygame.time.get_ticks() / 1000.0
        deltaTime = time - getTicksLastFrame
        getTicksLastFrame = time

        ###### UPDATE ETAT DES BATTES

        player1.update(deltaTime)
        player2.update(deltaTime)

        #end1.setPosition(player2.batte.end1[0], player2.batte.end1[1], player2.batte.end1[2])


        ###### SCORE UPDATE

        score1Texture = TextTexture(f"{score1}", (0, 0, 0), (255, 255, 255))
        if player1.score == 10:
            score1Texture = TextTexture("You Win", (0, 0, 0), (255, 255, 255))
            score2Texture = TextTexture("You Loose", (0, 0, 0), (255, 255, 255))
            #score1, score2 = 0, 0
        
        score2Texture = TextTexture(f"{score2}", (0, 0, 0), (255, 255, 255))
        if player2.score == 10:
            score1Texture = TextTexture("You loose", (0, 0, 0), (255, 255, 255))
            score2Texture = TextTexture("You win", (0, 0, 0), (255, 255, 255))
            #score1, score2 = 0, 0

        if player1.score < 10 and player2.score < 10:
            if len(ballManager.balls) == 0:
                service = True

            if sphere.position.z <= player1.position.z - 7:
                score2 += 1
                service = True
            if sphere.position.z >= player2.position.z + 7:
                score1 += 1
                service = True

            if service == True:
                # faut pouvoir en relancer une ici, donc faudrait créer un service
                sphere = Projectile("sphery", False, 1, battlefield, 'reflect', ballManager, scene)
                sphere.setPosition(0, 1, 0)
                sphere.setVelocity((random() - 0.5) / 2, (random() - 0.5) / 2, (random() - 0.5))
                sphereMat = TextureMaterial(sphereTex)
                sphere.setMaterial(sphereMat)

                player1.batte.isSuperBat = False
                player2.batte.isSuperBat = False

                battlefield.areViewsSwitched = False

                service = False

            for sphere in ballManager.balls:
                sphere.update(deltaTime)
                sphere.setRotationY(time * 50.0)
                sphere.setRotationX(time * 60.0)
                sphere.setRotationZ(time * 40.0)
                for mysteryBox in mysteryBoxes:
                    if mysteryBox.isCollision(sphere):
                        mysteryBox.onHit(sphere)

        else:
            for ball in ballManager.balls:
                ballManager.removeBall(ball)

            #### wait until you want to restart the game

        glEnable(GL_BLEND)

        ###### DESSIN DES SHAPES SUR FRAMEBUFFER

        ### PLAYER 1
        drawEyeToFrameBuffer(player1.rightEye, scene, rectMat, numTextures[1], score1Texture)
        drawEyeToFrameBuffer(player1.leftEye, scene, rectMat, numTextures[2], score1Texture)

        ### PLAYER 2
        drawEyeToFrameBuffer(player2.rightEye, scene, rectMat, numTextures[5], score2Texture)
        drawEyeToFrameBuffer(player2.leftEye, scene, rectMat, numTextures[6], score2Texture)

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

            if not battlefield.areViewsSwitched:
                interlacer.setTextureFromFBO(player1.rightEye.frameBuffer, 1)
                interlacer.setTextureFromFBO(player1.leftEye.frameBuffer, 2)

                interlacer.setTextureFromFBO(player2.rightEye.frameBuffer, 5)
                interlacer.setTextureFromFBO(player2.leftEye.frameBuffer, 6)

            else:
                interlacer.setTextureFromFBO(player2.rightEye.frameBuffer, 1)
                interlacer.setTextureFromFBO(player2.leftEye.frameBuffer, 2)

                interlacer.setTextureFromFBO(player1.rightEye.frameBuffer, 5)
                interlacer.setTextureFromFBO(player1.leftEye.frameBuffer, 6)

            interlacer.setTextureFromImage(blackTex, 3)
            interlacer.setTextureFromImage(blackTex, 4)

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
        if keys[pygame.K_x]:
            player1.setEyeDistance(player1.eyeDistance + 0.001)
            player2.setEyeDistance(player2.eyeDistance + 0.001)
        if keys[pygame.K_c]:
            player1.setEyeDistance(player1.eyeDistance - 0.001)
            player2.setEyeDistance(player2.eyeDistance - 0.001)
        if keys[pygame.K_v]:
            battlefield.areViewsSwitched = not battlefield.areViewsSwitched
        if keys[pygame.K_n]:
            service = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if player1.getGamepad() == None :
            if keys[pygame.K_z]:
                player1.batte.strike()
            if keys[pygame.K_q]:
                player1.batte.addRotationZ(1)
            if keys[pygame.K_d]:
                player1.batte.addRotationZ(-1)
        if player2.getGamepad() == None :
            if keys[pygame.K_UP]:
                player2.batte.strike()
            if keys[pygame.K_LEFT]:
                player2.batte.addRotationZ(-1)
            if keys[pygame.K_RIGHT]:
                player2.batte.addRotationZ(1)

            if event.type == pygame.MOUSEMOTION:
                x, y = event.rel
                if any(event.buttons):
                    model_matrix = model_matrix.dot(rotate(y, -1, 0, 0)).dot(rotate(x, 0, -1, 0))


            # pour tester si le programme detecte les appuie sur les boutons
        for i in range (nb_joystick) :
            gamepad[i].update()
            if gamepad[i].startButton() :
                service = True
                time = 0
                score1, score2 = 0, 0
            if gamepad[i].isBattePressed():
                if i == 0 :
                    player1.batte.strike()
                else :
                    player2.batte.strike()
            if gamepad[i].turnBatteLeft() :
                if (i == 0) and (player1.batte.position.x < 5) :
                    player1.batte.translate(0.1, 0, 0)
                if (i == 1) and (player2.batte.position.x < 5) :
                    player2.batte.translate(0.1, 0, 0)
            if gamepad[i].turnBatteRight() :
                if (i == 0) and (player1.batte.position.x > -5) :
                    player1.batte.translate(-0.1, 0, 0)
                if (i == 1) and (player2.batte.position.x > -5) :
                    player2.batte.translate(-0.1, 0, 0)
            if joystick[i].get_axis(0) != 0 :
                if i == 0 :
                    player1.batte.addRotationZ(-joystick[0].get_axis(0) * 1.5)
                if i == 1 :
                    player2.batte.addRotationZ(-joystick[1].get_axis(0) * 1.5)
        
        ''' keyboard.update()
        if keyboard.isBattePressed():
            print("batty")
        if nb_joystick > 0 :
            for i in range (nb_joystick) :
                gamepad[i].update()
                if gamepad[i].isBattePressed():
                    print("joybatty")'''