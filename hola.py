import pygame, sys
from pygame.locals import *
import random

#Number of frames per second
FPS = 10

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10

assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"
CELLWIDTH = WINDOWWIDTH // CELLSIZE # number of cells wide
CELLHEIGHT = WINDOWHEIGHT // CELLSIZE # Number of cells high

# set up the colours
BLACK =    (0,  0,  0)
WHITE =    (255,255,255)
DARKGRAY = (40, 40, 40)

#Draws the grid lines
def drawGrid():
    for x in range (0,WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y), (WINDOWWIDTH, y))
        
def colourGrid(item, lifeDict):
    x = item[0]
    y = item[1]
    y = y * CELLSIZE # translates array into grid size
    x = x * CELLSIZE # translates array into grid size
    if lifeDict[item] == 0:
        pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, CELLSIZE, CELLSIZE))
    if lifeDict[item] == 1:
        pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, CELLSIZE, CELLSIZE))
    return None

def blankGrid():
    gridDict = {}
    for y in range(CELLHEIGHT):
        for x in range(CELLWIDTH):
            gridDict[x, y] = 0
    return gridDict

def startingGridRandom(lifeDict):
    for item in lifeDict:
        lifeDict[item] = random.randint(0,1)
    return lifeDict

def getNeighbours(item,lifeDict):
    neighbours = 0
    for x in range (-1, 2):
        for y in range (-1, 2):
            checkCell = (item[0]+x,item[1]+y)
            if checkCell[0] < CELLWIDTH  and checkCell[0] >=0:
                if checkCell [1] < CELLHEIGHT and checkCell[1]>= 0:
                    if lifeDict[checkCell] == 1:
                        if x == 0 and y == 0: # negate the central cell
                            neighbours += 0
                        else:
                            neighbours += 1
    return neighbours

def tick(lifeDict):
    newTick = {}
    for item in lifeDict:
        numberNeighbours = getNeighbours(item, lifeDict)
        if lifeDict[item] == 1:# For those cells already alive
            if numberNeighbours < 2: # kill under-population
                newTick[item] = 0
            elif numberNeighbours > 3: #kill over-population
                newTick[item] = 0
            else:
                newTick[item] = 1 # keep status quo (life)
        elif lifeDict[item] == 0:
            if numberNeighbours == 3: # cell reproduces
                newTick[item] = 1
            else:
                newTick[item] = 0 # keep status quo (death)
    return newTick    

def main():
    pygame.init()
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
    pygame.display.set_caption('Hello World') 

    DISPLAYSURF.fill(WHITE) #fills the screen white
    lifeDict = blankGrid() # creates library and populates to match blank grid
    lifeDict = startingGridRandom(lifeDict)

    for item in lifeDict:
        colourGrid(item, lifeDict)

    drawGrid()
    pygame.display.update()

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #runs a tick
        lifeDict = tick(lifeDict)
        #Colours the live cells, blanks the dead
        for item in lifeDict:
            colourGrid(item, lifeDict)

        drawGrid()   
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()