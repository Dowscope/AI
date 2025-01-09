import random
import pygame

class Point:
    def __init__(self, width, height):
        self.x = random.randint(-width, width)
        self.y = random.randint(-height, height)
        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1

    def show(self, screen):
        if self.label == 1:
            pygame.draw.ellipse(screen, (0, 255, 0), (self.x, self.y, 10, 10))
        else:
            pygame.draw.ellipse(screen, (255, 0, 0), (self.x, self.y, 10, 10))