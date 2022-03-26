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