import math
import pygame

class Bullet:
    def __init__(self, launch_angle, init_pos):
        self.angle = launch_angle
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.SPEED = 10
        self.RADIUS = 5
        self.exists = True
        self.rect = pygame.rect.Rect(self.x - self.RADIUS, self.y - self.RADIUS, self.RADIUS * 2, self.RADIUS * 2)

    def loop(self, width, height):
        self.x += self.SPEED * math.sin(math.radians(self.angle))
        self.x = abs(self.x)
        self.y += self.SPEED * math.cos(math.radians(self.angle))
        self.rect = pygame.rect.Rect(self.x - self.RADIUS, self.y - self.RADIUS, self.RADIUS * 2, self.RADIUS * 2)

        if self.x + self.RADIUS >= width:
            self.exists = False

        if self.x - self.RADIUS <= 0:
            self.exists = False
        
        if self.y < 0:
            self.exists = False
            return True

        return False
            

    def draw(self, window):
        pygame.draw.circle(window, (255, 0, 0), (self.x, self.y), self.RADIUS)

