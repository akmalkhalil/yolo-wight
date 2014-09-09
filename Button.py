import pygame
from pygame.locals import *
#in hindsight i should have made two seperate classes and used inheritence somewhere
#maybe from a third parent/super class
#may have been easier

class Button():
    def __init__(self, rect, switch, text = "", Fsize = 12):
        self.rect = rect
        if isinstance(switch, bool):
            self.switch = switch
            self.onColour = pygame.color.Color(0,255,0)
            self.offColour = pygame.color.Color(255,0,0)
            self.colour = self.offColour
        elif isinstance(switch, list):
            self.switch = switch
            self.colour = pygame.color.Color(0,0,255)
            self.l = len(switch)
            self.stateN = 0 
        else:
            raise TypeError('switch must be a bool type or a list type')
        self.text = text
        self.Fsize = Fsize

    def pressButton(self):
        if isinstance(self.switch, bool):
            self.switch = not self.switch
        else:
            self.stateN += 1
            if self.stateN == self.l:
                self.stateN = 0

    def getState(self):
        if isinstance(self.switch, bool):
            return self.switch
        else:
            return self.switch[self.stateN]
        
            
        
    def showButton(self,surface):
        if isinstance(self.switch, bool):
            if self.switch:
                colour = self.onColour
            else:
                colour = self.offColour
        else:
            colour = self.colour
        pygame.draw.rect(surface, colour, self.rect)
        if len(self.text) > 0:
            font = pygame.font.Font('freesansbold.ttf',self.Fsize)
            msgSurfObj = font.render(self.text, False, pygame.color.Color(0,0,0))
            msgRectObj = msgSurfObj.get_rect()
            msgRectObj.center = (self.rect[0] + int(self.rect[2]/2), self.rect[1] + int(self.rect[3]/2))
            windowSurf.blit(msgSurfObj, msgRectObj)

        

    def Xstartstop(self):#the start and end of the x co-ords where button is
        return self.rect[0],self.rect[0]+self.rect[2]

    def Ystartstop(self):
        return self.rect[1],self.rect[1]+self.rect[3]
    
    

    




pygame.init()
fpsClock = pygame.time.Clock()
windowSurf = pygame.display.set_mode((640,480))
pygame.display.set_caption('buttons')
windowW = windowSurf.get_width()
windowH = windowSurf.get_height()

redCol = pygame.color.Color(255,0,0)
greenCol = pygame.color.Color(0,255,0)
blueCol = pygame.color.Color(0,0,255)
whiteCol = pygame.color.Color(255,255,255)
blackCol = pygame.color.Color(0,0,0)

b = Button((100,100,100,70),False, text = 'bob')
array = [redCol, greenCol, blueCol, whiteCol, blackCol]
b2 = Button((200,100,100,70),array)

mouseX,mouseY = 0,0

running = True
while running:
    windowSurf.fill(b2.getState())
    b2.showButton(windowSurf)
    b.showButton(windowSurf)

    if b.getState():
        pygame.draw.rect(windowSurf, whiteCol,(windowW/2-50, windowH/2 - 50, 100,100))
    else:
        pygame.draw.rect(windowSurf, whiteCol,(windowW/2-20, windowH/2 - 20, 40,40))

    pygame.display.update()
    fpsClock.tick(30)
    
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            mouseX,mouseY = event.pos
        elif event.type == QUIT:
            pygame.quit()
            running = False
        elif event.type == MOUSEBUTTONUP:
            b1X1,b1X2 = b.Xstartstop()
            b1Y1,b1Y2 = b.Ystartstop()
            b2X1,b2X2 = b2.Xstartstop()
            #b2Y1,b2Y2 = b2.Ystartstop()   don't need this as there on the same line
            if b1Y1 < mouseY < b1Y2:
                if b1X1 < mouseX < b1X2:
                    b.pressButton()
                elif b2X1 < mouseX < b2X2:
                    b2.pressButton()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q:
                pygame.event.post(pygame.event.Event(QUIT))
        
    
print('program end')
