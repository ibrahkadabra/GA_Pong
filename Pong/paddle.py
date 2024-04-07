import pygame

class Paddle:
    COLOR = (255, 255, 255)

    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.VEL = 5 

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)

    def move(self, up = True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.VEL = 5 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

