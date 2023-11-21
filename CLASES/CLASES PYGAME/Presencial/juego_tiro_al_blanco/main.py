import pygame
import sys
import random




class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        # Carga la imagen de la mira desde un archivo
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()  # Obtiene el rectángulo que rodea la imagen
        # Carga el sonido de disparo desde un archivo
        self.gunshot = pygame.mixer.Sound('shoot.mp3')

    def shoot(self):
        self.gunshot.play()  # Reproduce el sonido de disparo
        # Elimina los objetivos que se tocan
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        # Actualiza la posición de la mira para seguir el cursor del mouse
        self.rect.center = pygame.mouse.get_pos()




class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        # Carga la imagen del objetivo desde un archivo
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()  # Obtiene el rectángulo que rodea la imagen
        # Establece la posición inicial del objetivo
        self.rect.center = [pos_x, pos_y]




# Configuración general del juego
pygame.init()
clock = pygame.time.Clock()

# Configuración de la pantalla del juego
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Fondo del juego
# Carga la imagen de fondo desde un archivo
background = pygame.image.load('BG.png')
pygame.mouse.set_visible(False)  # Oculta el cursor del mouse

# Mira del jugador
crosshair = Crosshair('crosshair.png')  # Crea una instancia de la mira
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)  # Agrega la mira al grupo

# Objetivos
target_group = pygame.sprite.Group()
for target in range(10):
    new_target = Target('target.png', random.randrange(
        0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)  # Agrega objetivos al grupo

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Sale del juego si se cierra la ventana
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()  # Llama al método shoot() cuando se hace clic

    pygame.display.flip()  # Actualiza la pantalla
    screen.blit(background, (0, 0))  # Dibuja el fondo en la pantalla

    target_group.draw(screen)  # Dibuja los objetivos en la pantalla
    crosshair_group.draw(screen)  # Dibuja la mira en la pantalla

    crosshair_group.update()  # Actualiza la posición de la mira
    clock.tick(60)  # Controla la velocidad del juego a 60 cuadros por segundo
