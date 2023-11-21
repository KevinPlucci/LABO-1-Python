import pygame
from models.Bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed, stage_dict_configs: dict):
        super().__init__()

        self.__player_configs = stage_dict_configs.get('player')
        # Mostrar sprite del jugador
        self.image = pygame.image.load(self.__player_configs['player_img']).convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)

        # Atributos de movimiento
        self.speed = speed
        self.max_x_constraint = constraint

        # Atributos para disparar y recargar
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600
        self.bullet_group = pygame.sprite.Group()
        self.puntaje = 0

    def manejar_eventos_teclado(self):  # Eventos del jugador
        """
        The function handles keyboard events for player movement and shooting lasers.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:  # movimiento sobre eje x
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            #print(self.laser_time)

    @property
    def get_bullets(self) -> list[Bullet]:
        return self.bullet_group
    
    def shoot_laser(self):  # disparar laser
        print('!piu piu!')
        self.bullet_group.add(self.create_bullet())
    
    def create_bullet(self):
        return Bullet(self.rect.centerx, self.rect.top, 'up', True) # Crea y devuelve un objeto de la clase Bullet en la posición actual del ratón

    def recharge(self):
        if not self.ready:
            curent_time = pygame.time.get_ticks()
            if curent_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def constraint(self):  # Ajusta al jugador a los limites de la pantalla
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def update(self, screen: pygame.surface.Surface):
        self.manejar_eventos_teclado()
        self.constraint()
        self.recharge()
        self.bullet_group.draw(screen)
        self.bullet_group.update()
