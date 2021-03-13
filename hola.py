import pygame, sys
from pygame.locals import *
import random

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
GREEN =    (0,  255,0)

#Draws the grid lines
def drawGrid():
    for x in range (0,WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y), (WINDOWWIDTH, y))
        
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

def colourGrid(item, lifeDict):
    x = item[0]
    y = item[1]
    y = y * CELLSIZE # translates array into grid size
    x = x * CELLSIZE # translates array into grid size
    if lifeDict[item] ==0:
        pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, CELLSIZE, CELLSIZE))
    if lifeDict[item] == 1:
        pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, CELLSIZE, CELLSIZE))
    return None

def main():
    pygame.init()
    global DISPLAYSURF
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
        drawGrid()        
        pygame.display.update()

if __name__=='__main__':
    main()