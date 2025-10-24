import pygame
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import load_image

class Game:
    def __init__(self):
        pygame.init() # initializes pygame
        
        pygame.display.set_caption('Platformer')
        self.screen = pygame.display.set_mode((640, 480)) # initialize screen that's 640x480
        self.clock = pygame.time.Clock()
        self.movement = [False, False]
        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        
    def run(self):
        while True:
            self.screen.fill((14, 219, 248)) #fill screen with blue sky
            
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            for event in pygame.event.get(): # user input so window doesn't freeze
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # check if user pressed down on a key
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP: # check if user releases key
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(60) # set fps to 60 
    
Game().run()
    