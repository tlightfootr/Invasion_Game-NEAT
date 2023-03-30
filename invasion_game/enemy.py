import pygame
import random

class Enemy:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        self.RADIUS = 50
        self.x, self.y = random.randint(10, self.width - 10), random.randint(int(self.height * 1/3), int(self.height * 2/3))
        self.rect = pygame.rect.Rect(self.x - self.RADIUS, self.y - self.RADIUS, self.RADIUS * 2, self.RADIUS * 2)

    def generate_random_location(self):
        self.x, self.y = random.randint(10, self.width - 10), random.randint(int(self.height * 1/3), int(self.height * 2/3))
        self.rect = pygame.rect.Rect(self.x - self.RADIUS, self.y - self.RADIUS, self.RADIUS * 2, self.RADIUS * 2)

    def draw(self):
        pygame.draw.circle(self.window, (50, 50, 255), (self.x, self.y), self.RADIUS)