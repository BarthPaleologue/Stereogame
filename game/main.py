import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math

class Bomb(object):
    def __init__(self, aposX, aposY, bombRange=5):
        self.posX = aposX 
        self.posY = aposY
        self.bombRange = bombRange
        self.timeToExplode = 3000

    def update(self, dt):
        # Subtract the passed time `dt` from the timer each frame.
        self.timeToExplode -= dt

    def explode(self, screen):
        pygame.draw.line(screen,(200,0,0),(self.posX,self.posY),(self.posX+20+(40*self.bombRange),self.posY),40)
        pygame.draw.line(screen,(200,0,0),(self.posX,self.posY),(self.posX-20-(40*self.bombRange),self.posY),40)
        pygame.draw.line(screen,(200,0,0),(self.posX,self.posY),(self.posX,self.posY+20+(40*self.bombRange)),40)
        pygame.draw.line(screen,(200,0,0),(self.posX,self.posY),(self.posX,self.posY-20-(40*self.bombRange)),40)

    def draw(self, screen):
        pygame.draw.circle(screen,(200,0,0),(self.posX,self.posY),20)


def main():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    bomb_set = set()  # This set holds the bomb instances.

    done = False

    while not done:
        # Get the passed time since last clock.tick call.
        dt = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bomb_set.add(Bomb(*event.pos))

        # Game logic.
        to_remove = set()

        # Update bombs. Pass the `dt` to the bomb instances.
        for bomb in bomb_set:
            bomb.update(dt)
            # Add old bombs to the to_remove set.
            if bomb.timeToExplode <= -3000:
                to_remove.add(bomb)

        # Remove bombs fromt the bomb_set.
        if to_remove:
            bomb_set -= to_remove

        # Draw everything.
        screen.fill((30, 30, 30))
        for bomb in bomb_set:
            bomb.draw(screen)
            # I'm just drawing the explosion lines each
            # frame when the time is below 0.
            if bomb.timeToExplode <= 0:
                bomb.explode(screen)

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()