import pygame
import sys

class Game:
    def __init__(self):
        pygame.init() # initializes pygame
        
        pygame.display.set_caption('Platformer')
        self.screen = pygame.display.set_mode((640, 480)) # initialize screen that's 640x480

        self.clock = pygame.time.Clock() # declare clock for framerate
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0)) #transparent color key
        self.img_pos = [160, 260]
        self.movement = [False, False]
    def run(self):
        while True:
            self.screen.fill((14, 219, 248)) #fill screen with blue sky
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5 # only allows for one direction if both keys are pressed
            self.screen.blit(self.img, self.img_pos) # display cloud, top left is (0, 0)
            
            
            for event in pygame.event.get(): #user input so window doesn't freeze
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # check if user pressed down on a key
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP: # check if user releases key
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
                    
                    
            pygame.display.update()
            self.clock.tick(60) # set fps to 60 
    
Game().run()
    