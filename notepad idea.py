#you need a folder or directory called 'notes' in the same folder/directory as this file
#maybe i should do a try except further down to catch this




#don't know why but i decided to make a wiered not thingy
#atleast i learnt a little about ASCII and typing and things
#I;m bad with words
import pygame
from pygame.locals import *
from time import gmtime
from os import listdir
pygame.init()
fpsClock = pygame.time.Clock()
windowSurf = pygame.display.set_mode((640,480))
pygame.display.set_caption('this is my crappy notepas thingamabob')
windowW = windowSurf.get_width()
windowH = windowSurf.get_height()

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textL = ['']#L for lines

blackCol = pygame.color.Color(0,0,0)
whiteCol = pygame.color.Color(255,255,255)


running = True
while running:
    windowSurf.fill(blackCol)
    
    for i in range(len(textL)):
        textSurfObj = fontObj.render(textL[i],False,whiteCol)
        textRectObj = textSurfObj.get_rect()
        textRectObj.center = (windowW/2, 25 + i*32)
        windowSurf.blit(textSurfObj, textRectObj)

    pygame.display.update()
    fpsClock.tick()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False
        elif event.type == KEYDOWN:
            #print(event.key)
            #print(chr(event.key))
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_BACKSPACE:
                if len(textL) == 1 and len(textL[0]) == 0:
                    pass
                elif len(textL) > 1 and len(textL[-1]) == 0:
                    textL.pop()
                else:
                    textL[-1] = textL[-1][:-1]
            elif event.key == 13:
                textL.append('')
            elif event.key == K_s and pygame.key.get_mods() == 64:
                folder = listdir('notes')
                if len(folder) == 0:
                    name = '00'
                else:
                    lastN = int(folder[-1][-6:-4])
                    name = str(lastN+1) if lastN >= 9 else '0'+str(lastN + 1)
                pygame.image.save(windowSurf, 'notes/shot' + name + '.png')
                print(name)
                #if i want user to choose name
                #just do an input() and check if input in folder
            else:
                textL[-1] += str(chr(event.key))
                        
