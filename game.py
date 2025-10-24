import pygame
import sys

class Game:
    def __init__(self):
        pygame.init() # initializes pygame
        
        pygame.display.set_caption('Platformer')
        self.screen = pygame.display.set_mode((640, 480)) # initialize screen that's 640x480

        self.clock = pygame.time.Clock() # declare clock for framerate
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
    
    def run(self):
        while True:
            self.screen.blit(self.img, (100, 200)) # display cloud
            for event in pygame.event.get(): #user input so window doesn't freeze
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            
            pygame.display.update()
            self.clock.tick(60) # set fps to 60 
    
Game().run()
    