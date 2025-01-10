import random
import pygame

class Point:
    def __init__(self, width, height):
        self.RADIUS = 8
        self.IND_RADIUS = self.RADIUS / 2

        self.x = 0
        self.y = 0
        self.label = 0
        self.training = True

        self.reset(width, height)

    def show(self, screen):
        if self.label == 1:
            pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.RADIUS, 1)
        else:
            pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.RADIUS)

        if not self.training:
            pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), self.IND_RADIUS)
        else:
            pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.IND_RADIUS)

    def reset(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1
        self.training = True