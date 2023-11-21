import pygame
from constantes import screen_h

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # self.image = pygame.Surface((50, 10))
        # self.image.fill((255, 0, 0))
        self.image = pygame.image.load('./space_invaders_parte_1/graphics/player_laser.png')
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.y -= 20

        if self.rect.y <= 0:
            self.kill()