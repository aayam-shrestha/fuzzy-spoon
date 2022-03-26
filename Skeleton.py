import os, sys, math, pygame, pygame.mixer
from pygame.locals import *

#creates a window and screen of a set size
width, height = 1375, 1000
character_width, character_height = 100, 100
win = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Platofrmer") #Window Title

fps_limit = 60 #Refresh Rate

#Import Background
bg = pygame.image.load('Forrest_Level.png')
bg = pygame.transform.scale(bg, (width, height))

#Import Character Image
character = pygame.image.load('final_form.png')
character = pygame.transform.scale(character, (character_width, character_height))

#Flip Character Image
flipped_char = pygame.transform.flip(character, True, False)

global isJump
isJump = False

#Draw Character Facing Right
def draw_right(ferret):
    screen.blit(character, (ferret.x, ferret.y))
    pygame.display.update()

#Draw Character Facing Left
def draw_left(ferret):
    screen.blit(flipped_char, (ferret.x, ferret.y))
    pygame.display.update()
    
#Draw Rectangle
def draw_platform(x, y, width, height):
    color = (0, 0, 0)
    pygame.draw.rect(win, color, pygame.Rect(x, y, width, height))
    
def collisions(ferret, item):
    collide = pygame.Rect.colliderect(ferret, item)
    if collide:
        if isJump == True and ferret.y < item.y:
            ferret.bottom = item.top
        if isJump == False and ferret.y > item.y and ferret.right > item.left and ferret.y + 100 > item.y + 100:
            ferret.right = item.left
            
def pos_check(ferret, lvl0):
    for item in lvl0:
       # print(ferret.bottom, item.top)
        if ferret.bottom == item.top and ((ferret.left > item.left and ferret.left + 100 < item.right) or (ferret.right < item.right and ferret.right - 100 > item.left)):
            return 0
        elif (ferret.left > item.left and ferret.left + 100 < item.right) or (ferret.right < item.right and ferret.right - 100 > item.left):
            return item.top - ferret.bottom
    return height - ferret.bottom

#Main Body
def main():
    
    run_me = True #Game Runs
    clock = pygame.time.Clock() #Frame Rate
    pygame.display.update()
    
    ferret = pygame.Rect(100, 650, character_width, character_height) #Makes image an Object
    lvl0_start = pygame.Rect(0, 750, 400, 400)
    lvl0_log1 = pygame.Rect(437, 650, 500, 30)
    lvl0_mid = pygame.Rect(975, 500, 400, 600)
    lvl0_log2 = pygame.Rect(437, 350, 500, 30)
    lvl0_end = pygame.Rect(0, 200, 400, 100)
    lvl0 = [lvl0_start, lvl0_log1, lvl0_mid, lvl0_log2, lvl0_end]
    
    m = 1
    v = 10
    airtime = 0
    
    #Jump Mechanics
    global isJump
    isJump = False
    
    #Character Facing Movement Direction
    character_is_right = True

    #Keep Game Running till Manual Quit
    while run_me:
        clock.tick(fps_limit) 

        win.blit(bg, (0,0)) #Constant Background Display
        
        draw_platform(0, 750, 400, 400)
        collisions(ferret, lvl0_start)
        
        draw_platform(437, 650, 500, 30)
        collisions(ferret, lvl0_log1)
        
        draw_platform(975, 500, 400, 600)
        collisions(ferret, lvl0_mid)
        
        draw_platform(437, 350, 500, 30)
        collisions(ferret, lvl0_log2)
        
        draw_platform(0, 200, 400, 100)
        collisions(ferret, lvl0_end)
            
        #Exit Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_me = False
        
        #Arrow Controls
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            ferret.x -= 5
            character_is_right = False
            
        if keys[pygame.K_RIGHT]:
            ferret.x += 5
            character_is_right = True

        if keys[pygame.K_SPACE]:
            if pos_check(ferret, lvl0) == 0:
                isJump = True

        #https://www.geeksforgeeks.org/python-making-an-object-jump-in-pygame/
        if isJump:
            F = (1/2)* m *( v **2)
            ferret.y -= F
            v = v-1
            if v<0:
#                 m= -1
#             if v == -10:
                isJump = False
                v =10
                m =1
        else:
            #GRAVITY
            platform_dist = pos_check(ferret, lvl0);
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
            draw_right(ferret)
        if not character_is_right:
            draw_left(ferret)

        pygame.display.update()
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()
