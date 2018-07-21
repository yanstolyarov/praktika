import pygame
import time
pygame.init()
screen_width=240
screen_height=70
screen=pygame.display.set_mode([screen_width,screen_height])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("SPACE")
                pygame.quit();
    time.sleep(1)
