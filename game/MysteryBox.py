from feather.materials.textureMaterial import TextureMaterial
from feather.shapes.cube import Cube
from feather.texture import Texture
import random
allEffects = {1:'disparition',2:'teleport',3:'bomb',4:'x3',5:'superbat'}
class MysteryBox(Cube):
    

    # battlex is the attribute size_x of the battlefield, and same thing for battley and battlez
    def __init__(self,name, battlefield, scene = None):
        Cube.__init__(self, name,True, scene)
        self.battlex, self.battley, self.battlez = battlefield.getSizex(), battlefield.getSizey(), battlefield.getSizez()
        boxMat = TextureMaterial(Texture("./assets/question.jpeg"))
        self.setMaterial(boxMat)
        self.setPosition(random.uniform(-self.battlex,self.battlex),random.uniform(-self.battley,self.battley),random.uniform(-self.battlez,self.battlez))

    def isCollision(self, ball):
        ballposition = ball.getPosition()
        x,y,z = ballposition[0], ballposition[1], ballposition[2]
        position = self.getPosition()
        bx, by, bz = position[0],position[1],position[2]
        if abs(bx-x)<= 1.5 and abs(by-y)<= 1.5 and abs(bz-z)<= 1.5:
            return True
        return False
    
    def onHit(self,ball):
        x,y,z = self.battlex, self.battley, self.battlez
        self.setPosition(random.uniform(-x+1, x-1), random.uniform(-y + 2, y-2), random.uniform(-3, 3))
        effect = 2
        #effect = random.randint(1,4)
        ball.applyEffect(allEffects[effect])







