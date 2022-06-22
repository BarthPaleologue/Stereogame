
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from fileLoader import *


if __name__ == "__main__":
    pygame.init()
    display = (1000,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_PROJECTION) # <---- specify projection matrix
    gluPerspective(90, (display[0]/display[1]), 0.1, 100)

    glMatrixMode(GL_MODELVIEW)  # <---- specify model view matrix
    glTranslatef(0.0, 0.0, -5)

    # import file
    model = OBJ('hammer.obj', swapyz=True)
    angle =0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # draw model
        glPushMatrix()
        

        model.render()
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == KEYDOWN: #fleche gauche augmente angle de rotation, droite diminue
                if event.key == K_LEFT:
                    angle += 1
                elif event.key == K_RIGHT:
                    angle -= 1
                glRotatef(angle, 3, 1, 1)
        
        
        