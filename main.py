from game import Game, Button
import pygame, sys
from platforms import Platform

width, height = 1375, 1000
win = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((width, height))
pygame.font.init()
font = pygame.font.SysFont('Calibri', 72)
menu_bg = pygame.image.load('menu_bg.jpg')
menu_bg = pygame.transform.scale(menu_bg, (width, height))

def main_menu():
    while True:
        screen.blit(menu_bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = font.render("FUZZY FRANKY", True, "#002147")
        MENU_RECT = MENU_TEXT.get_rect(center=(650, 450))

        PLAY_BUTTON = Button(pos=(450, 600),
                            text_input="PLAY", font = font, base_color="#000080", hovering_color="White")
        HELP_BUTTON = Button(pos=(650, 600),
                            text_input="HELP", font = font, base_color="#000080", hovering_color="White")
        QUIT_BUTTON = Button(pos=(850, 600),
                            text_input="QUIT", font = font, base_color="#000080", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, HELP_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    g = Game(win,screen, width, height)
                    g.main()
                if HELP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    help_info()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def help_info():

    texts = ['','Control functions:','Use left and right arrow to move', 'Press space to jump', '', 'Goals:', 'Avoid all the obstacles', 'Reach the end point']
    font = pygame.font.Font('freesansbold.ttf', 20)
   
    for i in range(8):
       
        textsurface = font.render(texts[i], True, (0, 0, 0))
        screen.blit(textsurface,(500,700+ i*20))
        pygame.display.flip()
   
    pygame.time.wait(3000)
    
main_menu()

