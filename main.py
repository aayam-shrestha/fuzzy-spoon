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
            if event.key == pygame.K_LEFT:
                posx = posx - 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                posx = posx + 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                posy = posy - 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                posy = posy + 10
                
    screen.blit(picture, (posx, posy))
    pygame.display.update()
    pygame.display.flip()

    

pygame.quit()
