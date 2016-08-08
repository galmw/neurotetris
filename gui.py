import pygame
import time
from pygame import *
import sys

pygame.init()


windowSize = 768, 1024
screen = pygame.display.set_mode(windowSize)
screen.fill([255,255,255])

#TODO remove
board = [[0 if (i+j) % 2 == 0 else 1 for j in xrange(10)] for i in xrange(10)]

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
blue = (0, 0, 255)
colors = [white, black ,red, blue]

blockSize = 40

#def printBlock()
## Pictures:
#doodlePicture = pygame.image.load("doodleNinjaPicture.png")
#background = pygame.image.load("Picture.jpg")
#background.convert()
#backgroundRect = background.get_rect()
#screen.blit(background, backgroundRect)



while True:

    time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for i in xrange(10):
        for j in xrange(10):
            if (board[i][j]):
                draw.rect(screen,black,(i*50 + 50,j*50 + 50,blockSize,blockSize))

    pygame.display.update()



