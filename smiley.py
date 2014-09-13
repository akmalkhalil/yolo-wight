import pygame
from pygame.locals import *
from math import pi, sin, cos, radians

pygame.init()
fpsClock = pygame.time.Clock()
windowSurf = pygame.display.set_mode((640,480))
pygame.display.set_caption('smiley thingy, damn it i am soo bored')
windowW = windowSurf.get_width()
windowH = windowSurf.get_height()

redCol = pygame.color.Color(255,0,0)
blueCol = pygame.color.Color(0,0,255)
greenCol = pygame.color.Color(0,255,0)
blackCol = pygame.color.Color(0,0,0)
whiteCol = pygame.color.Color(255,255,255)

count = 0
spin = False
surf2 = pygame.Surface((windowW, windowH))


running = True
while running:
    windowSurf.fill((0,0,0))
    windowSurf.blit(surf2, (0,0))
    

    #pygame.draw.circle(surf2, blueCol, (int(windowW/4), int(windowH/3)), 50, 3)
    #pygame.draw.circle(surf2, blueCol, (int(windowW/4)*3, int(windowH/3)),50,3)


    if spin:
##        count +=5
        surf2 = pygame.transform.rotate(surf2, 1)
##        if count == 360:
##            count = 0
##            spin = False
    
    for i in range(1,4,2):
        pygame.draw.circle(surf2, whiteCol, (int(windowW/4)*i, int(windowH/3)), 45)
        pygame.draw.circle(surf2, blueCol, (int(windowW/4)*i, int(windowH/3)), 50,5)
        pygame.draw.circle(surf2, blackCol, (int(windowW/4)*i, int(windowH/3)), 6)


##    for i in range(1,20):
##        pygame.draw.line(surf2, redCol, (windowW/2, windowH/2), (windowW/2 + (windowW/4)*cos(i%pi),windowH/2 + (windowH/4)*sin(i%pi)) )
    for i in range(1,20):
        pygame.draw.circle(surf2, greenCol,(int(windowW/2 + (windowW/4)*cos(i%pi)),30+int(windowH/2 + (windowH/4)*sin(i%pi))), 20, 1) 
    pygame.display.update()
    fpsClock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()#you know do the usual change it thing
                running = False
            elif event.key == K_SPACE:
                surf2 = pygame.Surface((windowW, windowH))
        elif event.type == MOUSEBUTTONUP:
##            if not spin:
##                spin = True
            spin = not spin




print('program end')
