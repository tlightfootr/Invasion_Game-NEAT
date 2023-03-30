from .bullet import Bullet
import pygame
import math
import time

class Player:
    def __init__(self, width, height):
        self.window_width = width
        self.window_height = height
        self.angle = 180
        self.MIN_ANGLE = 250
        self.MAX_ANGLE = 110
        self.ROTATE_SPEED = 0.7
        self.bullet_list = []
        self.img = pygame.transform.scale_by(pygame.image.load('cannon.png'), (0.5, 0.5))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = self.window_width / 2 - self.width / 2
        self.y = self.window_height - self.height
        self.shots_missed = 0

    def indicator(self):
        DISTANCE = 30
        SIZE = 10
        x = self.window_width / 2 + DISTANCE * math.sin(math.radians(self.angle)) - SIZE / 2
        y = self.window_height - self.height + DISTANCE * math.cos(math.radians(self.angle)) - SIZE / 2
        return pygame.rect.Rect(x, y, 10, 10)

    def rotate(self, cw=True):
        if cw:
            if self.angle > self.MAX_ANGLE:
                self.angle -= self.ROTATE_SPEED
        else:
            if self.angle < self.MIN_ANGLE:
                self.angle += self.ROTATE_SPEED

    def shoot(self):
        self.bullet_list.append(Bullet(self.angle, (self.window_width / 2, self.window_height - self.height)))

    def loop(self):
        for i in self.bullet_list:

            if i.exists == True:
                if i.loop(self.window_width, self.window_height):
                    self.shots_missed += 1

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
        pygame.draw.rect(window, (0, 255, 255), self.indicator())

        for i in self.bullet_list:
            if i.exists == True:
                i.draw(window)


