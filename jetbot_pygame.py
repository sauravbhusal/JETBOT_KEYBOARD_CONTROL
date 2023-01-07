
import pygame
import sys
#import os
#os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()

display = pygame.display.set_mode((300,300))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            file = open('keyboard.txt','w')

            if event.key == pygame.K_w:
                print ("keypress = forward")
                file.write('8')


            if event.key == pygame.K_s:
                print ("keypress = backward")
                file.write('2')

            if event.key == pygame.K_a:
                print ("keypress = left")
                file.write('4')

            if event.key == pygame.K_d:
                print ("keypress = right")
                file.write('6') 

            
            if event.key == pygame.K_q:
                print ("keypress = stop")
                file.write('0')  

            if event.key == pygame.K_t:
                print ("keypress = turbo")
                file.write('1')        

            file.close()   