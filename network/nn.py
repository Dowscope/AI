#!/usr/bin/python3

import pygame
from Perceptron import Perceptron
from Point import Point

NUM_POINTS = 100
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
POINTS = [Point(SCREEN_WIDTH, SCREEN_HEIGHT) for _ in range(NUM_POINTS)]

def render(screen):
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    for point in POINTS:
        point.show(screen)

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        render(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()



if __name__ == "__main__":
    main()