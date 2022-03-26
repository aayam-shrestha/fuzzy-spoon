
import os, sys, math, pygame, pygame.mixer
from pygame.locals import *
from platforms import Platform

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
        self.bg = pygame.image.load('Forest_Level.png')
        self.bg = pygame.transform.scale(self.bg, (width, height))
        
        #import Character Image
        self.character = pygame.image.load('final_form.png')
        self.character = pygame.transform.scale(self.character, (self.character_width,self.character_height))
        
        self.isJump = False

        #Flip Character Image
        self.flipped_char = pygame.transform.flip(self.character, True, False)
    
        self.p1 = Platform(self.screen)

    #Draw Character Facing Right
    def draw_right(self,ferret):
        self.screen.blit(self.character, (ferret.x, ferret.y))
        pygame.display.update()
     
     #Draw Character Facing Left
    def draw_left(self,ferret):
        self.screen.blit(self.flipped_char, (ferret.x, ferret.y))
        pygame.display.update()
  
    def check_collisions(self, ferret):
        item = self.p1.collisions(ferret)
        if item:
            if self.isJump == True and ferret.y < item.y:
                ferret.bottom = item.top
            if self.isJump == False and ferret.y > item.y and ferret.right > item.left and ferret.y + 100 > item.y + 100:
                ferret.right = item.left
    
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
        lvl0=[]
        for item in self.p1.platf:
            lvl0.append(pygame.Rect(item))
        #Character Facing Movement Direction
        character_is_right = True
 
        while run_me:
            clock.tick(self.fps_limit)

            self.win.blit(self.bg, (0,0))
            self.p1.draw(self.screen, "black")

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
                    print(drop_dist)
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


class Hazard:
   
    def __init__(self, screen):
#         self.posx = pos[0]
#         self.posy = pos[1]
        self.hazard_pos = [[670,320], [700, 500]]
        h_rect = []
        self.color = (100, 100, 100)
        self.screen = screen
       
    def draw(self):
       
        for i in self.hazard_pos:
            h_rect.append(pygame.Rect(i[0] - 30, i[1], 60, 50))
            pygame.draw.polygon(surface= self.screen, color=self.color, points=[(self.posx - 30, self.posy + 50), (self.posx,self.posy), (self.posx+ 30, self.posy + 50)])
       
        pygame.display.flip()
       
    def collisions(self,ferret, item):
        collide = pygame.Rect.colliderect(ferret, item)
        if collide:
            if self.isJump == True and ferret.y < item.y:
                ferret.bottom = item.top
            if self.isJump == False and ferret.y > item.y and ferret.right > item.left and ferret.y + 100 > item.y + 100:
                ferret.right = item.left

###Make a charcter class and check hit between character and r
