
import os, sys, math, pygame, pygame.mixer
from pygame.locals import *
from platforms import Platform, Hazard

class Game:
      
    def __init__(self, window, screen, width, height):
        self.win = window
        self.screen = screen
        self.width = width 
        self.height = height
        
        self.character_width, self.character_height = 200, 200

        pygame.display.set_caption("Platformer") #window title

        self.fps_limit = 60
        
        #import Background
        self.bg = pygame.image.load('Game_bg.png')
        self.bg = pygame.transform.scale(self.bg, (width, height))
        
        #import Character Image
        self.character = pygame.image.load('final_form.png')
        self.character = pygame.transform.scale(self.character, (self.character_width,self.character_height))
        
        self.isJump = False

        #Flip Character Image
        self.flipped_char = pygame.transform.flip(self.character, True, False)
    
        self.p = Platform(self.screen)
        self.h = Hazard(self.screen)
#         self.c = Coin(self.screen)


    #Draw Character Facing Right
    def draw_right(self,ferret):
        self.screen.blit(self.character, (ferret.x, ferret.y))
        pygame.display.update()
     
     #Draw Character Facing Left
    def draw_left(self,ferret):
        self.screen.blit(self.flipped_char, (ferret.x, ferret.y))
        pygame.display.update()
  
    def check_collisions(self, ferret):
        
        item = self.p.collisions(ferret)
        if item:
            if self.isJump == True and ferret.y < item.y:
                ferret.bottom = item.top
            if self.isJump == False and ferret.y > item.y and ferret.right > item.left and ferret.y + 100 > item.y + 100:
                ferret.right = item.left
        
        hazard = self.h.collisions(ferret)
        if hazard or (ferret.bottom == self.height):
            gameover = pygame.font.SysFont('Calibri', 120)
            text = gameover.render("Game Over!", True, (255,0,0))
            self.screen.blit(text, (550, 500))
            pygame.display.flip()
            pygame.time.wait(3000)
            sys.exit()
            
#         coin = self.c.collisions(ferret)




    def pos_check(self, ferret, lvl0):
        for item in lvl0:
           # print(ferret.bottom, item.top)
            if ferret.bottom == item.top and ((ferret.left > item.left and ferret.left + 100 < item.right) or (ferret.right < item.right and ferret.right - 100 > item.left)):
                return 0
            elif (ferret.left > item.left and ferret.left + 100 < item.right) or (ferret.right < item.right and ferret.right - 100 > item.left):
                return item.top - ferret.bottom
        return self.height - ferret.bottom   
    
    def main(self):
       
        run_me = True #game runs
        clock = pygame.time.Clock() #Frame rate
        pygame.display.update()
        
        m = 1
        v = 9
        airtime = 0
        ferret = pygame.Rect(100, 675, self.character_width, self.character_height) #makes image an object
        self.lvl0=[]
        for item in self.p.platf:
            lvl0.append(pygame.Rect(item))
        #Character Facing Movement Direction
        character_is_right = True
 
        while run_me:
            clock.tick(self.fps_limit)

            self.win.blit(self.bg, (0,0))
            self.p.draw(self.screen, "black")
            self.h.draw(self.screen, "red")
            
            self.check_collisions(ferret)

           #Exit game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_me = False
                   
            #Arrow controls
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                ferret.x -= 5
                character_is_right = False
                
            if keys[pygame.K_RIGHT]:
                ferret.x += 5
                character_is_right = True

            if keys[pygame.K_SPACE]:
                if self.pos_check(ferret, lvl0) == 0:
                    self.isJump = True

             #https://www.geeksforgeeks.org/python-making-an-object-jump-in-pygame/
            if self.isJump:
                F = (1/2)* m *( v **2)
                ferret.y -= F
                v = v-1
                if v<0:
                    m= -1
                if v == -10:
                    self.isJump = False
                    v =9
                    m =1
            else:
                #GRAVITY
                platform_dist = self.pos_check(ferret, lvl0)
                if platform_dist == 0:
                    airtime = 0
                else:
                    airtime += 1
                    drop_dist =  min(platform_dist, (1/2) * (airtime**2))
                    ferret.y += drop_dist
            #Boundaries
            if ferret.x < 0:
                ferret.x = 0
            if ferret.x > 1175:
                ferret.x = 1175
            
            
            #Character Direction
            if character_is_right:
                self.draw_right(ferret)
            if not character_is_right:
                self.draw_left(ferret)
                
            pygame.display.update()
            pygame.display.flip()
       
        pygame.quit()




class Button:
    def __init__(self, pos, text_input,font, base_color, hovering_color):

        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
