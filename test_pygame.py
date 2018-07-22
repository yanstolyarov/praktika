import pygame, sys
from pygame.locals import *
import time

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('P.Earth')
#while 1: # main game loop
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.display.update()



#direction = ''
#print('Welcome to Earth')
#pygame.draw.rect(screen, RED, [55,500,10,5], 0)
#time.sleep(1)





pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

textsurface = myfont.render('Some Text', False, (0, 0, 0))
screen.blit(textsurface,(0,0))
