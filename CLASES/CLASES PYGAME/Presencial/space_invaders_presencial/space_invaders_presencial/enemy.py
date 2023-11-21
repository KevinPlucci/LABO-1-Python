import pygame
import random as rd
import time  # Agregado para medir el tiempo


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, constraint_x, constraint_y, speed):
        super().__init__()

        # Mostrar sprite del jugador
        self.avatar = self.seleccionar_avatar()
        self.image = pygame.image.load(
            f"./space_invaders_parte_1/graphics/{self.avatar}.png"
        ).convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)

        # Atributos de movimiento
        self.speed = speed
        self.max_x_constraint = constraint_x
        self.max_y_constraint = constraint_y
        self.frame_rate = 120
        self.time_move = 0
        self.move_right = True

    def seleccionar_avatar(self):
        avatar = rd.choice(["yellow", "red", "green"])
        return avatar

    def constraint(self):  # Ajusta al jugador a los limites de la pantalla
        if self.move_right:
            if self.rect.right < self.max_x_constraint:
                # self.rect.left += self.speed
                self.rect.x += self.speed * 2
            else:
                if self.rect.bottom < self.max_y_constraint:
                    # self.rect.bottom += self.speed
                    self.rect.y += self.speed * 3
                self.move_right = False
        else:
            if self.rect.left > 0:
                # self.rect.right -= self.speed
                self.rect.x -= self.speed * 2
            else:
                if self.rect.bottom < self.max_y_constraint:
                    # self.rect.bottom += self.speed
                    self.rect.y += self.speed * 3
                self.move_right = True

    def do_movement(self, delta_ms):
        self.time_move += delta_ms
        if self.time_move >= self.frame_rate:
            self.constraint()

    def update(self, delta_ms):
        self.do_movement(delta_ms)
        # self.constraint()

    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)
