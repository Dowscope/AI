#!/usr/bin/python3

import pygame
from Perceptron import Perceptron
from Point import Point

NUM_POINTS = 1000
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
POINTS = [Point(SCREEN_WIDTH, SCREEN_HEIGHT) for _ in range(NUM_POINTS)]
BRAIN = Perceptron(2)

def reset():
    for point in POINTS:
        point.reset(SCREEN_WIDTH, SCREEN_HEIGHT)

def render(screen):
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
     
    for point in POINTS:
        point.show(screen)

def update():
    for point in POINTS:
        inputs = [point.x, point.y]
        target = point.label
        guess = BRAIN.guess(inputs)
        if guess == target:
            point.training = False
        else:
            point.training = True

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                  for point in POINTS:
                      inputs = [point.x, point.y]
                      target = point.label
                      BRAIN.train(inputs, target)


        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        render(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        update()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()



if __name__ == "__main__":
    main()