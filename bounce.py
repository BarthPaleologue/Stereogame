from OpenGL.GL import *
import numpy as np
import pygame

#local imports
from feather import Texture, FrameBuffer, Scene, Screen
from feather.shapes import Rectangle, Cube, Sphere
from feather.materials import ColorMaterial, TextureMaterial
from feather.projections import *
from feather.algebra import *
from feather.camera import *
from feather.shapes.sphere import Sphere
from interlacer import Interlacer

from game import Player, Battlefield
from game.ball import  Ball

if __name__ == "__main__":
    pygame.init()
    #width, height = 1920, 1080
    infoObject = pygame.display.Info()
    width, height = infoObject.current_w, infoObject.current_h
    pygame.display.set_mode((width, height), pygame.DOUBLEBUF|pygame.OPENGL|pygame.HWSURFACE, 0)
    #pygame.display.toggle_fullscreen()

    scene = Scene()
    
    ######## DECLARATION DES SHAPES

    sphere = Ball("sphery", False,1, scene)
    sphere.setPosition(-2, -3, 2)
    sphere.setScaling(0.3, 0.3, 0.3)
    sphere.setVelocity(0.01, 0.02, 0)
    sphereMat = TextureMaterial(Texture("./assets/tennis.png"))
    sphere.setMaterial(sphereMat)

    """

    sphere = Ball("sphery", False,  1,scene)
    #sphere = Ball("sphery", position = [-5,-6,0], velocity = [0.001,0.001,0.001], radius =  scene = scene)
    ##sphere = Ball("sphery", radius = 1, scene = scene)
    sphere.setPosition(-6, -3, 0)
 #   sphere.setVelocity(0.001, 0.001, 0.001)
    sphere.setScaling(0.3, 0.3, 0.3)
    sphereMat = TextureMaterial(Texture("./assets/tennis.png"))
    sphere.setMaterial(sphereMat)"""

    battlefield = Battlefield("battly", 7, 7, 7, scene)
    battleMat = TextureMaterial(Texture("./assets/textBattle.jpeg"))
    battlefield.setMaterial(battleMat)

    #gun = OBJsanstex("./assets/awp.obj", False, scene)
    
    rect = Rectangle('rect', False, scene)
    rect.setPosition(-6, -3, 0)
    rect.setScaling(0.5, 0.5, 1)

    rectMat = ColorMaterial(1.0, 0.0, 0.0)
    rect.setMaterial(rectMat)
    
    ######### DECLARATION DE L'ECRAN

    screen = Screen('screen')

    ######### MATRICES UTILES

    perspective_mx = perspective(45, width / height, 0.1, 100)
    model_matrix = np.identity(4, dtype=np.float32)
    ortho_mx = ortho(-1, 1, 1, -1, -50, 50)
    ident_matrix = np.identity(4, dtype=np.float32)

    ######### DECLARATION DES JOUEURS
    
    player1 = Player(False, None)
    player1.setPosition(0, 0, -5)
    player2 = Player(False, None)
    player2.setPosition(0, 0, -5)

    fbo_width = int(width/2)
    fbo_height = int(height/2)

    ######### DECLARATION DE L'ENTRELACEUR

    interlacer = Interlacer()

    ######### DECLARATION DES VARIABLES DE LA BOUCLE

    getTicksLastFrame = 0.0
    x,z = 0.0, 0.0
    circleRadius = 1.7

    ######### GAME LOOP

    running = True
    while running:
        time = pygame.time.get_ticks() / 1000.0
        deltaTime = time - getTicksLastFrame
        getTicksLastFrame = time

        ###### UPDATE ETAT DES SHAPES

        #pygame.time.wait(1000)

        sphere.update()
        print(sphere.getPosition())
        
        if battlefield.isCollision(sphere.getRadius(), sphere.getPosition()):
            print("COLLISION")
            vectors = battlefield.normalVector(battlefield.whereCollision(sphere.getRadius(), sphere.getPosition()))
            normVect = vectors
            #wallVect = vectors[1]
            oldVelocity = sphere.getVelocity()

            newVelocity = reflection(oldVelocity, normVect)

            sphere.setVelocity(newVelocity[0], newVelocity[1], newVelocity[2])

            #normal = np.multiply(normVect,np.dot(oldVelocity, np.multiply(normVect, -1)))
            #tangent = np.multiply(wallVect,np.dot(oldVelocity, wallVect))
            #print(oldVelocity)
            #newVelocity = np.add(np.multiply(normVect,np.dot(oldVelocity, np.multiply(normVect, -1))), np.multiply(wallVect,np.dot(oldVelocity, wallVect)))
            #print( "vectors : ", vectors , "newVolicty : " ,newVelocity)
            #sphere.setVelocity(newVelocity)
    #########################        sphere.update()

        ###### DESSIN DES SHAPES SUR FRAMEBUFFER

        fbo = player1.oeilGauche.frameBuffer
        fbo.bind()
        glViewport(0, 0, fbo_width, fbo_height)

        scene.render(player1.oeilGauche.getProjectionMatrix(), model_matrix, player1.oeilGauche.computeViewMatrix())

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

        interlacer.setTextureFromFBO(fbo, 0)
        interlacer.setTextureFromFBO(fbo, 1)
        interlacer.setTextureFromFBO(fbo, 2)
        interlacer.setTextureFromFBO(fbo, 3)
        interlacer.setTextureFromFBO(fbo, 4)
        interlacer.setTextureFromFBO(fbo, 5)
        interlacer.setTextureFromFBO(fbo, 6)
        interlacer.setTextureFromFBO(fbo, 7)

        screen.draw(interlacer.program)



        pygame.display.flip() # why do we need that tho ?

        ####### GESTION DES ENTREES CLAVIER

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            circleRadius += 0.05
        if keys[pygame.K_s]:
            circleRadius -= 0.05

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            """
            if event.type == pygame.KEYDOWN:
                sphere.update()"""
            if event.type == pygame.MOUSEMOTION:
                x, y = event.rel
                if any(event.buttons):
                    
                    model_matrix = model_matrix.dot(rotate(y, -1, 0, 0)).dot(rotate(x, 0, -1, 0))