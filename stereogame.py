from random import random
from OpenGL.GL import *
from feather.materials.shaderMaterial import ShaderMaterial
import numpy as np
from game.main import Bomb
from game.player.GamePad import GamePad
from game.player.Keyboard import Keyboard
import pygame

#local imports
from feather import Texture, Scene, Screen
from feather.shapes import Rectangle, Cube
from feather.materials import ColorMaterial, TextureMaterial
from feather.projections import *
from feather.algebra import *
from feather.camera import *
from interlacer import Interlacer
from feather.loaders.RowOBJ import RowOBJ
from game import Player, Battlefield
from game.ball import  Ball
from game.Bomb import Bomb

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

    # object 10485_Baseball_bat_v1_max8
    bat = RowOBJ("./assets/baseball/batB.obj", False, scene)
    bat.setPosition(0, 0, 0)
    batMat = TextureMaterial(Texture("./assets/baseball/wood.jpg"))
    batMat2 = ColorMaterial(0.5, 0.5, 0.5)
    bat.setMaterial(batMat)

    battlefield = Battlefield("battly", 10, 6, 20, scene)
    battleMat = TextureMaterial(Texture("./assets/textBattle.jpeg"))
    #battleMat2 = ShaderMaterial("./game/battlefieldMat/vertex.glsl", "./game/battlefieldMat/fragment.glsl")
    #battleMat2.updateFunction = lambda battleMat2:
    #battleMat2.setUniform("u_time", pygame.time.get_ticks() / 1000.0)
        
    battlefield.setMaterial(battleMat)

    sphereTex = Texture("./assets/space.png")

    spheres = []
    for i in range(10):
        sphere = Ball("sphery", False, 1, battlefield, scene)
        sphere.setPosition(-2, 0, 0)
        sphere.setVelocity((random() - 0.5) / 10.0, (random() - 0.5) / 10.0, (random() - 0.5) / 10.0)
        sphereMat = TextureMaterial(sphereTex)
        sphere.setMaterial(sphereMat)
        spheres.append(sphere)

    bat = RowOBJ("./assets/baseball/batB.obj",False,scene)
    #bat.setScaling(0.5,0.5,0.5)
    bat.setPosition(0,0,0)
    batMat = TextureMaterial(Texture("./assets/Baseball/wood.jpg"))
    bat.setMaterial(batMat)
    #skull = OBJ("./assets/skull.obj", False, scene)
    #for(i, shape) in enumerate(skull.shapes):
    #	shape.setScaling(0.05, 0.05, 0.05)
    #	shape.setRotationX(90)

    battlefield = Battlefield("battly", 14, 6, 20, scene)
    #battleMat = TextureMaterial(Texture("./assets/textBattle.jpeg"))
    #battlefield.setMaterial(battleMat)

    #gun = OBJsanstex("./assets/awp.obj", False, scene)
    
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
    
    player1 = Player(False, None)
    player1.setPosition(0, 0, -10)
    player2 = Player(True, None)
    player2.setPosition(0, 0, 10)

    player3 = Player(False, None)
    player3.setPosition(0, 0, -7)

    fbo_width = int(width/2)
    fbo_height = int(height/2)

    ######### DECLARATION DE L'ENTRELACEUR

    interlacer = Interlacer()

    ######### DECLARATION DES VARIABLES DE LA BOUCLE

    getTicksLastFrame = 0.0
    x,z = 0.0, 0.0
    circleRadius = 2.5

    ######### GAME LOOP
    buttons = Keyboard()

    pygame.joystick.init()
    if pygame.joystick.get_count() > 0 :
        joystick = pygame.joystick.Joystick(0)
        joy = GamePad(0)
    
    running = True
    while running:
        time = pygame.time.get_ticks() / 1000.0
        deltaTime = time - getTicksLastFrame
        getTicksLastFrame = time

        ###### UPDATE ETAT DES SHAPES

        bat.addRotationZ(20.0 * deltaTime)
        
        yellow_cube.addRotationY(deltaTime * 70.0).addRotationX(deltaTime * 80.0)

        rotationSpeed = 1
        x = math.cos(time * rotationSpeed) * circleRadius
        z = math.sin(time * rotationSpeed) * circleRadius

        yellow_cube.setPosition(x, 0, z)

        """for sphere in spheres:
            if battlefield.isCollision(sphere.getRadius(), sphere.getPosition()):
                normVect = battlefield.normalVector(battlefield.whereCollision(sphere.getRadius(), sphere.getPosition()))
                oldVelocity = sphere.getVelocity()
                newVelocity = reflection(oldVelocity, normVect)

                sphere.setVelocity(newVelocity[0], newVelocity[1], newVelocity[2])

        
            sphere.update()
            sphere.setRotationY(time * 50.0)
            sphere.setRotationX(time * 60.0)
            sphere.setRotationZ(time * 40.0)"""
        for bomb in spheres:
            if battlefield.isCollision(bomb.getRadius(), bomb.getPosition()):
                bomb.explode()
            bomb.update()
            bomb.setRotationY(time * 50.0)
            bomb.setRotationX(time * 60.0)
            bomb.setRotationZ(time * 40.0)
            


        ###### DESSIN DES SHAPES SUR FRAMEBUFFER

        ### PLAYER 1
        drawEyeToFrameBuffer(player1.oeilDroit, scene, rectMat,  numTextures[1])
        drawEyeToFrameBuffer(player1.oeilGauche, scene, rectMat,  numTextures[2])

        ### SEPARATION
        #drawEyeToFrameBuffer(player3.oeilDroit, scene, rectMat, numTextures[3])
        #drawEyeToFrameBuffer(player3.oeilGauche, scene, rectMat,  numTextures[4])

        ### PLAYER 2
        drawEyeToFrameBuffer(player2.oeilDroit, scene, rectMat,  numTextures[5])
        drawEyeToFrameBuffer(player2.oeilGauche, scene, rectMat,  numTextures[6])

        ### SEPARATION
        #drawEyeToFrameBuffer(player3.oeilDroit, scene, rectMat,  numTextures[7])
        #drawEyeToFrameBuffer(player3.oeilGauche, scene, rectMat,  numTextures[0])
        

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

            interlacer.setTextureFromFBO(player1.oeilDroit.frameBuffer, 1)
            interlacer.setTextureFromFBO(player1.oeilGauche.frameBuffer, 2)
            #interlacer.setTextureFromImage(blackTex, 0)
            #interlacer.setTextureFromImage(blackTex, 1)

            #interlacer.setTextureFromFBO(player3.oeilDroit.frameBuffer, (2 + offset) % 8)
            #interlacer.setTextureFromFBO(player3.oeilGauche.frameBuffer, (3 + offset) % 8)
            interlacer.setTextureFromImage(blackTex, 3)
            interlacer.setTextureFromImage(blackTex, 4)
            
            interlacer.setTextureFromFBO(player2.oeilDroit.frameBuffer, 5)
            interlacer.setTextureFromFBO(player2.oeilGauche.frameBuffer, 6)
            #interlacer.setTextureFromImage(blackTex, 4)
            #interlacer.setTextureFromImage(blackTex, 5)

            #interlacer.setTextureFromFBO(player3.oeilDroit.frameBuffer, (6 + offset) % 8)
            #interlacer.setTextureFromFBO(player3.oeilGauche.frameBuffer, (7 + offset) % 8)
            interlacer.setTextureFromImage(blackTex, 7)
            interlacer.setTextureFromImage(blackTex, 0)

        else:
            interlacer.setTextureFromFBO(player1.oeilDroit.frameBuffer, 0)
            interlacer.setTextureFromFBO(player1.oeilDroit.frameBuffer, 1)
            interlacer.setTextureFromFBO(player1.oeilDroit.frameBuffer, 2)
            interlacer.setTextureFromFBO(player1.oeilDroit.frameBuffer, 3)
            interlacer.setTextureFromFBO(player1.oeilDroit.frameBuffer, 4)
            interlacer.setTextureFromFBO(player1.oeilDroit.frameBuffer, 5)
            interlacer.setTextureFromFBO(player1.oeilDroit.frameBuffer, 6)
            interlacer.setTextureFromFBO(player1.oeilDroit.frameBuffer, 7)

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
            #player3.setEyeDistance(player3.eyeDistance + 0.001)
        if keys[pygame.K_d]:
            player1.setEyeDistance(player1.eyeDistance - 0.001)
            player2.setEyeDistance(player2.eyeDistance - 0.001)
            #player3.setEyeDistance(player3.eyeDistance - 0.001)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.rel
                if any(event.buttons):
                    model_matrix = model_matrix.dot(rotate(y, -1, 0, 0)).dot(rotate(x, 0, -1, 0))
            # pour tester si le programme detecte les appuie sur les boutons
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
        

        
        buttons.update()
        if buttons.isBattePressed():
            print("batty")
        if pygame.joystick.get_count() > 0 :
            joy.update()
            if joy.isBattePressed():
                print("joybatty")
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            circleRadius += 0.05
        if keys[pygame.K_s]:
            circleRadius -= 0.05
