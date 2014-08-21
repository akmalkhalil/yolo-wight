import pygame, math
from pygame.locals import *
pygame.init()
fpsClock = pygame.time.Clock()
windowSurf = pygame.display.set_mode((640,480))
pygame.display.set_caption('algorithmic drawing test 2')
windowW = windowSurf.get_width()
windowH = windowSurf.get_height()

colour = {
    'red' : pygame.Color(255,0,0),
    'green' : pygame.Color(0,255,0),
    'blue' : pygame.Color(0,0,255),
    'white' : pygame.Color(255,255,255),
    'magenta' : pygame.Color(255,0,255),
    'yellow' : pygame.Color(255,255,0),
    'cyan' : pygame.Color(0,255,255),
    'black' : pygame.Color(0,0,0),
    'silver' : pygame.Color(192,192,192)
}
count = 0
running = True
sides = 10
bg = 'black'
while running:
    windowSurf.fill(colour[bg])
##    pygame.draw.circle(windowSurf,colour['red'], (int(windowW/2),int(windowH/2)), int(20 +10*math.sin(count)), 1)
##    pygame.draw.circle(windowSurf, colour['blue'], (int(windowW/2+10*math.sin(count)), int(windowH/2+10*math.cos(count))), 20, 1)
    
    count += 0.1

##    for i in range(10):
##        pygame.draw.line(windowSurf, colour['green'], (windowW/2+40*math.sin((i/10)*math.pi), windowH/2+40*math.cos((i/10)*math.pi)), (windowW/2+40*math.sin((i/10+1)*math.pi), windowH/2+40*math.cos((i/10+1)*math.pi) ) )

    for i in range(10):
        pygame.draw.circle(windowSurf, colour['magenta'], (int(windowW/2 + math.sin(i/10 * 2 * math.pi * count)*i*10),int(windowH/2 + math.cos(i/10 * 2 * math.pi * count)*i*10)), 15,1)

    
##    for i in range(sides):
##        pygame.draw.line(windowSurf, colour['cyan'], (int(windowW/2 + math.sin( i/sides * 2 * math.pi) * 40), int(windowH/2 + math.cos( i/sides * 2 * math.pi)*40)),(int(windowW/2 + math.sin( (i+1)/sides * 2 * math.pi) * 40), int(windowH/2 + math.cos( (i+1)/sides * 2 * math.pi)*40)) )
    #now i wanna do summat with this to make it move
    pygame.display.update()
    fpsClock.tick(30)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
        elif event.type == MOUSEBUTTONDOWN:
            if bg == 'black':
                bg = 'white'
            elif bg == 'white':
                bg = 'black'
    #print(count)
                
print('buh bye')
print('count =',count)
