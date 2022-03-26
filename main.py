from game import Game
import pygame
from platforms import Platform

width, height = 1375, 1000
win = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((width, height))
g = Game(win,screen, width, height)
g.main()


       


