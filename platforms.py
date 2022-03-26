import pygame

class Platform:
    def __init__(self, screen):

        self.platf = [(0, 750, 400, 400), (437, 650, 500, 30), (975, 500, 400, 600), (437, 350, 500, 30), (0, 200, 400, 100)]

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
            

    
    