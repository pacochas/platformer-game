import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480)) # initialize screen that's 640x480

clock = pygame.time.Clock() # declare clock for framerate

while True:
    for event in pygame.event.get(): #user input so window doesn't freeze
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    
    
    pygame.display.update()
    clock.tick(60) # set fps to 60 
    
    