import pygame
from game.player.Input import Input

class GamePad(Input):

    # initializing all buttons states to False
    def __init__(self,id):
        self.id = id
        self.buttons = None
        self.before = self.buttons # the state of keys before modification
        n = pygame.joystick.Joystick(id).get_numbuttons()
        print("the number of buttons is " + str(n))
        self.buttons = []
        for i in range(n):
            self.buttons.append(False)
        
        

    def update(self):
        self.before = self.buttons
        n = len(self.buttons)
        for i in range(n):
            self.buttons[i] = pygame.joystick.Joystick(self.id).get_button(i)
        
    def isBattePressed(self):
        bool = self.buttons[6] and (not self.before[6])
        return bool

    def getEffectButton(self, effect):
        if effect == "batte":
            return self.buttons[3] and (not self.before[3])
        elif effect == "explosion":
            return self.buttons[2] and (not self.before[2])

