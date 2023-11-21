from models.auxiliar import SurfaceManager as sf
import pygame as pg
from models.constantes import ANCHO_VENTANA, ALTO_VENTANA, FPS, DEBUG
from models.player.main_player import (
    Jugador,
)  # Importar la clase Jugador desde el archivo del jugador


class Enemigo:
    def __init__(self, coord_x, coord_y, speed=5, gravity=16):
        self.__move_x = coord_x
        self.__move_y = coord_y
        self.__speed = speed
        # Utilizar las mismas imágenes del jugador para el enemigo
        self.__enemy_animation = sf.get_surface_from_spritesheet(
            "./assets/img/player/iddle/player_idle.png", 5, 1
        )
        self.__initial_frame = 0
        self.__enemy_img = self.__enemy_animation[self.__initial_frame]
        self.__rect = self.__enemy_img.get_rect()
        self.__is_looking_right = True
        self.__gravity = gravity

    def __set_x_animations_preset(self):
        self.__rect.x -= self.__speed
        if self.__speed < 0:
            # Si el enemigo se mueve hacia la izquierda, invertir la imagen horizontalmente
            self.__enemy_img = pg.transform.flip(
                self.__enemy_animation[self.__initial_frame], True, False
            )
        else:
            self.__enemy_img = self.__enemy_animation[self.__initial_frame]

    def __set_borders_limits(self):
        if self.__rect.right < 0:
            self.__rect.left = ANCHO_VENTANA
        return 0  # Cambiado para siempre devolver 0

    def do_movement(self):
        self.__rect.x -= self.__speed
        print(f"Enemigo X: {self.__rect.x}, Y: {self.__rect.y}")

        # Verificar si el enemigo ha alcanzado el límite izquierdo o derecho de la pantalla
        if self.__rect.left < 0 or self.__rect.right > ANCHO_VENTANA:
            # Invertir la dirección del movimiento
            self.__speed = -self.__speed
        if self.__rect.y < 300:
            self.__rect.y += self.__gravity

        # Aplicar movimiento vertical (si es necesario)

    def do_animation(self):
        self.__initial_frame = (self.__initial_frame + 1) % len(self.__enemy_animation)
        if self.__speed < 0:
            self.__enemy_img = pg.transform.flip(
                self.__enemy_animation[self.__initial_frame], True, False
            )
        else:
            self.__enemy_img = self.__enemy_animation[self.__initial_frame]

    def update(self, delta_ms):
        self.do_movement()
        self.do_animation()

    def draw(self, screen: pg.surface.Surface):
        if DEBUG:
            pg.draw.rect(screen, "red", self.__rect)
        screen.blit(self.__enemy_img, self.__rect)
