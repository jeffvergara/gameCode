import pygame
from pygame.locals import *
import sys
import random

BOARDWIDTH = 4
BOARDHEIGTH = 4
TILESIZE = 80
WINDOWWIDTH = 640
WINDOWHEIGTH = 480
FPS = 30
BLANK = None

# RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (0, 240, 0)
GREEN = (0, 204, 0)

BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MASSAGECOLOR = WHITE


XMARGIN = int((WINDOWWIDTH- (TILESIZE * BOARDWIDTH + (BOARDHEIGTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGTH - (TILESIZE * BOARDHEIGTH + (BOARDHEIGTH - 1))) / 2)

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "rigth"

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGTH)
    pygame.display.set_caption("Slide Puzzle")
    BASICFONT = pygame.font.Font("freesansbold.ttf", BASICFONTSIZE)


    #store the option buttons and their rectangles in OPTIONS.

    RESET_SURF, RESET_RECT = makeText("Reset", TEXTCOLOR,TILECOLOR,WINDOWWIDTH - 120, WINDOWHEIGTH - 90)
    NEW_SURF, NEW_RECT = makeText("New game", TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGTH - 60)
    SOLVE_SURF, SOLVE_RECT = makeText("Solve", TEXTCOLOR, TILECOLOR, WINDOWWIDTH- 120, WINDOWHEIGTH - 30)

    mainBoard, solutionSeq = generateNewPuzzle(80)
    SOLVEBOARD = getStartingBoard() # a solved board is the same as the board in a start state.
    allMove = [] #list of all move made from the solved configuration.

    while True: # game main loop
        slideTo = None #the direction, if any, a tile should slide.
        msg = "" #contains the message to show the upper left corner

        if mainBoard == SOLVEBOARD:
            msg = "SOLVED"

        drawBoard(mainBoard, msg)

        checkForQuit()
        for event in pygame.event.get(): #event handling loop
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0])


                if (spotx, spoty) == (None, None)
                    #check if the user clicked on an option button
                    if RESET_RECT.collidepoint(event.pos):







