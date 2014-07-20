import pygame, time, sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
windowSurf = pygame.display.set_mode((980,480))
windowH= windowSurf.get_height()
windowW = windowSurf.get_width()
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
colour2 = {}
file = open ('C:\\Users\\Akmal\\Desktop\\Files\\500+ colours.csv','r')
lines = file.readlines()
file.close
colName = ''
red = 0
green = 0
blue =0
for i in range(1,len(lines)):
    row = lines[i].split(',')
    colName = str(row[0])
    red,green,blue = int(row[4]),int(row[5]),int(row[6])
    colour2[colName] = pygame.color.Color(red,green,blue)

bg = colour2["lawngreen"]

car = pygame.image.load('car.png')
car = pygame.transform.scale(car, (80,40))
carX = 20
v = 0

tree1 = pygame.image.load('tree1.png')
tree2 = pygame.image.load('tree2.png')
tree2 = pygame.transform.scale(tree2, (int(tree2.get_width()/100), int(tree2.get_height()/100)))

grass = tree2.get_height()+20


fontObj = pygame.font.Font('freesansbold.ttf', 32)
msg = 'playing'


numTrees = random.randint(4,7)
treeX = [random.randint(grass,windowW-grass) for x in range(numTrees)]#random.randint(grass,windowW-grass)
treeY = []
for i in range(numTrees):
    if random.randint(1,2) == 1:
        treeY.append(5)
    else:
        treeY.append(windowH-grass)


playing = True

carStartY = grass +20 #constant
carY = carStartY #variable


crashFX = pygame.mixer.Sound('car_crash.wav')


def accel():
    global v
    v +=1

def decel():
    global v
    v -= 1


def drawFinish():
    rectStart = (windowW-50, 0)
    rectD = (20,windowH) #D for dimensions
    pygame.draw.rect(windowSurf, colour['white'], (windowW-50, 0, 20, windowH))
    pixArr = pygame.PixelArray(windowSurf)
    for x in range(windowW-50,windowW-30, 2):
        for y in range(0,windowH,4):
            if x % 4 == 2:
                pixArr[x][y] = colour['black']
                pixArr[x+1][y] = colour['black']
                pixArr[x][y+1] = colour['black']
                pixArr[x+1][y+1] = colour['black']
            else:
                pixArr[x][y+2] = colour['black']
                pixArr[x+1][y+2] = colour['black']
                pixArr[x][y+3] = colour['black']
                pixArr[x+1][y+3] = colour['black']
            
    del pixArr


while playing:
    #the green grass
    windowSurf.fill(bg)
    #the gray road
    pygame.draw.rect(windowSurf, colour2['gray 40'], (0, grass, windowW, windowH-grass*2))
    drawFinish()
    windowSurf.blit(car,(carX,carY))#drawing the car
    #drawing the white lines
    for i in range(3):
        pygame.draw.line(windowSurf, colour['white'], (0,(carStartY+i*80 + car.get_height()+20)),(windowW,(carStartY+i*80 + car.get_height()+20)))
    
    #different tree locations drawn every game
    for i in range(numTrees):
        windowSurf.blit(tree2, (treeX[i],treeY[i]))
        if carY in range(treeY[i], treeY[i] + tree2.get_height()):
            if carX+ car.get_width() > treeX[i] and carX+ car.get_width() < treeX[i]+tree2.get_width():
                v=0
                crashFX.play()
                carX, carY = 20,carStartY

    #no -ve velocity which kinda defeats the point of calling it velocity
    if v > 0:
        carX += v

    if carX+car.get_width() >= windowW-50:
        msg = 'CONGRATULATIONS'
        v=0
    msgSurfObj = fontObj.render(msg, False, colour['blue'])
    msgRectObj = msgSurfObj.get_rect()
    msgRectObj.center = (windowW/2,20)
    windowSurf.blit(msgSurfObj, msgRectObj)
        

    #now lets see if it hits a tree
    

    pygame.display.update()
    fpsClock.tick(30)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            playing = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            elif event.key == K_RIGHT:
                accel()
            elif event.key == K_LEFT:
                if v != 0:
                    decel()
            elif event.key == K_DOWN:
                if carY + car.get_height() <= windowH-grass+20:
                    carY +=80
            elif event.key == K_UP:
                if carY >= grass+20:
                    carY -=80
print('GAME FINISHED')
