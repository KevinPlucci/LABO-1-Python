import pygame
import sys
import random


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("shoot.mp3")

    def shoot(self):
        self.gunshot.play()
        # Elimina los objetivos que se tocan y registra el blanco acertado
        targets_hit = pygame.sprite.spritecollide(self, target_group, True)
        return sum(target.score for target in targets_hit)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y, size, score):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.score = score


# Configuración general del juego
pygame.init()
clock = pygame.time.Clock()

# Configuración de la pantalla del juego
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Fondo del juego
background = pygame.image.load("BG.png")
pygame.mouse.set_visible(False)

# Mira del jugador
crosshair = Crosshair("crosshair.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Objetivos
target_group = pygame.sprite.Group()
for _ in range(10):
    size = (random.randint(50, 100), random.randint(50, 100))
    score = random.randint(1, 10)
    new_target = Target(
        "target.png",
        random.randrange(0, screen_width),
        random.randrange(0, screen_height),
        size,
        score,
    )
    target_group.add(new_target)

# Tiempo del juego
start_time = pygame.time.get_ticks()
game_duration = 30000

# Puntos totales
total_points = 0

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            points = crosshair.shoot()
            total_points += points

    pygame.display.flip()
    screen.blit(background, (0, 0))

    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()

    elapsed_time = pygame.time.get_ticks() - start_time
    remaining_time = max(0, (game_duration - elapsed_time) // 1000)
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f"Time: {remaining_time} seconds", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

    points_text = font.render(f"Points: {total_points}", True, (255, 255, 255))
    screen.blit(points_text, (10, 50))

    if elapsed_time >= game_duration:
        pygame.quit()
        sys.exit()

    clock.tick(60)
