from .player import Player
from .enemy import Enemy
import pygame
import time

class GameInformation:
    def __init__(self, score):
        self.score = score

class Game:
    def __init__(self, window, width, height):
        self.player = Player(width, height)
        self.enemy = Enemy(window, width, height)
        self.window = window
        self.width, self.height = width, height
        self.score = 0

    def collision(self):
        for i in self.player.bullet_list:
            if i.exists:
                if i.rect.colliderect(self.enemy.rect):
                    self.enemy.generate_random_location()
                    i.exists = False
                    self.score += 1    
    
    def draw(self):
        self.window.fill((0, 0, 0))
        self.player.draw(self.window)
        self.enemy.draw()

    def loop(self):
        self.player.loop()
        self.collision()

        return GameInformation(self.score)