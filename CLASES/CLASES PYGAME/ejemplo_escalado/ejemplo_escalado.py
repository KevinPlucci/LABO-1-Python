import pygame
import sys


class GameObject(pygame.sprite.Sprite):
    def __init__(self, image_path, pos_x, pos_y, scale=1.0):
        super().__init__()

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image,(int(screen_width * scale), int(screen_height * scale)))
        self.rect = self.image.get_rect()
        self.rect.x = int(screen_width * pos_x)
        self.rect.y = int(screen_height * pos_y)
    
    def draw(self):
        screen.blit(self.image, self.rect)


class Player(GameObject):
    def __init__(self, image_path, pos_x, pos_y, scale=1.0):
        super().__init__(image_path, pos_x, pos_y, scale)
    

class Level(GameObject):
    def __init__(self, image_path, pos_x, pos_y):
        super().__init__(image_path, pos_x, pos_y)
    

class Game:
    def __init__(self):
        self.level = Level('./subway_2.jpg', 0, 0) # subway_1.jpg
        self.player = Player('./cyclops_sprite.png', 0.03, 0.6, 0.3) # subway 1 (0.03, 0.3, 0.3)
    
    def run(self):
        self.level.draw()
        self.player.draw()


# -------------------------------------

pygame.init()
clock = pygame.time.Clock()
fps = 60

# Config Ventana
screen_width, screen_height = 854, 480 # 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Instancia principal
game = Game()

# Bucle principal
while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    game.run()
    
    pygame.display.update()