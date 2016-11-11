import pygame, sys
from pygame.locals import *
import threading
import time
import math
#import pywin32

windowW = 500
windowH = 400
rectW=80
rectH=10
rectX=windowW/2
rectY=windowH-2*rectH
rectDelta = 10

circleX=math.floor(windowW/2)
circleY=10
circleR=10
direction="down"

game_over = False

def move_circle():
    global direction, circleY, rectDelta, game_over
    while True:
        if direction=="down":
            if circleY < rectY-circleR:
                circleY=circleY+rectDelta
            elif circleX > rectX and circleX < rectX+rectW and circleY <= rectY and circleY >= rectY-circleR:
                direction="up"
            else:
                game_over=True
                #win32api.MessageBox(0,"Game over", "title")
        elif direction=="up":
            if circleY > circleR:
                circleY=circleY-rectDelta
            else:
                direction="down"
        time.sleep(0.2)
    
def draw_circle(disp):
    global circleX, circleY, circleR
    GREEN=(0,255,0)
    #print("Circle center at ({0},{1})".format(circleX, circleY))
    pygame.draw.circle(disp,GREEN, (circleX,circleY), circleR)

def main():
    global windowW,windowH,rectW,rectH,rectX,rectY,rectDelta

    pygame.init()
    pygame.display.set_caption("Adem's PingPong Game")

    DISPLAY=pygame.display.set_mode((windowW,windowH),0,32)

    WHITE=(255,255,255)
    blue=(0,0,255)
    RED=(255,0,0)

    DISPLAY.fill(WHITE)
    pygame.draw.rect(DISPLAY,blue,(rectX,rectY, rectW,rectH))
    pygame.key.set_repeat(50, 50);

    timer=threading.Timer(0.5, move_circle)
    timer.start() # runs once

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key == K_LEFT:
                    if (rectX > rectDelta):
                        rectX = rectX -rectDelta
                    else:
                        rectX = 0
                if event.key == K_RIGHT:
                    if (rectX < windowW - rectW):
                        rectX = rectX +rectDelta
                    else:
                        rectX = windowW - rectW
                #if event.key == K_UP:
                #    if (rectY > rectDelta):
                #        rectY = rectY -rectDelta
                #    else:
                #        rectY = 0
                #if event.key == K_DOWN:
                #    if (rectY < windowH - (rectH+rectDelta)):
                #        rectY = rectY +rectDelta
                #    else:
                #        rectY = windowH-rectH


        DISPLAY.fill(WHITE)
        pygame.draw.rect(DISPLAY,blue,(rectX,rectY, rectW,rectH))
        draw_circle(DISPLAY)
        if game_over:
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("Hello, World", True, (0, 128, 0))
            DISPLAY.blit(text)
            pygame.draw.rect(DISPLAY,RED,(windowW/2,windowH/2, rectW,rectH))
            
        pygame.display.update()

main()
