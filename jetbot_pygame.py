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
                print("key W has been pressed") 

            if event.key == pygame.K_s:
                print("key S has been pressed")

            if event.key == pygame.K_a:
                print("key A has been pressed")

            if event.key == pygame.K_d:
                print("key D has been pressed")
                
                               