import pygame

class Platform:
    def __init__(self, screen):

        self.platf = [(0, 800, 250, 50), (150, 700, 100, 100), (340, 550, 250, 50), (0, 0, 50, 350), (50, 300, 300, 50), (650, 950, 200, 50), (900, 850, 200, 50), (1150, 750, 200, 50), (900, 525, 250, 50), (600, 0, 50, 400), (650, 350, 300, 50), (1150, 250, 250, 50)]

        self.screen = screen
    
    def draw(self, screen, color):
        for i in self.platf:
            pygame.Rect(i)
            pygame.draw.rect(self.screen, color , i)

    def collisions(self,ferret):
        for item in self.platf:
            collide = pygame.Rect.colliderect(ferret, pygame.Rect(item))
            if collide:
                return pygame.Rect(item)
        return False
            

class Hazard:
   
    def __init__(self, screen):
        self.hazard_pos = [[670,320, 40, 50], [700, 500, 40, 50]]
        self.screen = screen
       
    def draw(self, screen, color):
       
        for i in self.hazard_pos:
            pygame.Rect(i)
            pygame.draw.rect(self.screen, color , i)
       
        pygame.display.flip()
       
       
    def collisions(self,ferret):
        for item in self.hazard_pos:
            collide = pygame.Rect.colliderect(ferret, pygame.Rect(item))
            if collide:
                return pygame.Rect(item)
        return False
        
class Coin:
    def __init__(self, screen):
        self.coins = [[700,500, 40, 50]]
        self.screen = screen
       
    def draw(self, screen, color):
       
        for i in self.coins:
            pygame.Rect(i)
            pygame.draw.rect(self.screen, color , i)
       
        pygame.display.flip()
       
       
    def collisions(self,ferret):
        for item in self.hazard_pos:
            collide = pygame.Rect.colliderect(ferret, pygame.Rect(item))
            if collide:
                return pygame.Rect(item)
        return False
        


    
    