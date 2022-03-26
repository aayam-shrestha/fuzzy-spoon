import os, sys, math, pygame, pygame.mixer
from pygame.locals import *

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
run_me = True

screen_size = screen_width, screen_height = 1000, 500
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('platformer')

window = pygame.display.set_mode((1000,500))
clock = pygame.time.Clock()
fps_limit = 60

picture = pygame.image.load('download.png')
bg = pygame.image.load('tree.png')

##bg = pygame.transform.scale(bg, screen_size)

posx = 300
posy = 200

while run_me:
    clock.tick(fps_limit) 

    window.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            run_me = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
    keys = pygame.key.get_pressed()
            
    posx += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 10
    posy += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 10
    
    posx = posx % window.get_width()
    posy = posy % window.get_height()
                
    screen.bli t(picture, (posx, posy))
    pygame.display.update()
    pygame.display.flip()

    

pygame.quit()
