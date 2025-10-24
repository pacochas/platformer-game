import pygame


class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos) # list of positions of entities
        self.size = size
        self.velocity = [0, 0]
    def update(self, movement = (0, 0)):
        # simple 2D vector
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]
    
    def render(self, surface):
        surface.blit(self.game.assets['player'], self.pos)
    