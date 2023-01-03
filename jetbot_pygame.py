import pygame
import sys

pygame.init()

display = pygame.display.set_mode((100, 100))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                keypress = 8

            if event.key == pygame.K_s:
                keypress = 2

            if event.key == pygame.K_a:
                keypress = 4

            if event.key == pygame.K_d:
                keypress = 6
                
                               