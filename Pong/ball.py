import pygame
from random import uniform

class Ball :
    MAX_VEL = 5

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL 
        self.y_vel = uniform(-self.MAX_VEL//10, self.MAX_VEL//10)


    def draw(self, win):
        pygame.draw.circle(win, (255,255,255), (self.x, self.y), self.radius)

  
    def move(self):
        self.x += self.x_vel 
        self.y += self.y_vel 

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.x_vel = -abs(self.x_vel)//self.x_vel * self.MAX_VEL
        self.y_vel = uniform(-self.MAX_VEL//10, self.MAX_VEL//10)

