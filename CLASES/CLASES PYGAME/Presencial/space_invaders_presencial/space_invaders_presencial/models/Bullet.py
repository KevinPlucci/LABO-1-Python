import pygame
from auxiliar.constantes import screen_h

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction, img_path = False):
        super().__init__()
        # self.image = pygame.Surface((50, 10))
        # self.image.fill((255, 0, 0))
        self.__load_img(img_path)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.direction = direction

    def __load_img(self, img_path: bool):
        if img_path:
            self.image = pygame.image.load('./assets/graphics/player_laser.png')
        else: 
            self.image = pygame.Surface((4, 20))
            self.image.fill('white')

    def update(self):
        
        match self.direction:
            case 'down':
                self.rect.y += 20
                if self.rect.y >= screen_h:
                    self.kill()
            case 'up':
                self.rect.y -= 20
                if self.rect.y <= 0:
                    self.kill()