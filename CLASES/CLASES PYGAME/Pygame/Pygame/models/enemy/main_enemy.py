from models.auxiliar import SurfaceManager as sf
import pygame as pg
from models.constantes import ANCHO_VENTANA, ALTO_VENTANA, FPS, DEBUG


class Enemigo:

    def __init__(self, coord_x, coord_y, speed=5):
        self.__move_x = coord_x
        self.__move_y = coord_y
        self.__speed = speed
        # Utilizar las mismas imágenes del jugador para el enemigo
        self.__enemy_animation = sf.get_surface_from_spritesheet('./assets/img/player/iddle/player_idle.png', 5, 1)
        self.__initial_frame = 0
        self.__enemy_img = self.__enemy_animation[self.__initial_frame]
        self.__rect = self.__enemy_img.get_rect()
        self.__is_looking_right = True

    def __set_x_animations_preset(self):
        self.__move_x -= self.__speed

    def __set_borders_limits(self):
        pixels_move = 0
        if self.__move_x + self.__rect.width < 0:
            self.__move_x = ANCHO_VENTANA
        return pixels_move

    def do_movement(self):
        self.__rect.x += self.__set_borders_limits()
        self.__set_x_animations_preset()

    def do_animation(self):
        if self.__initial_frame < len(self.__enemy_animation) - 1:
            self.__initial_frame += 1
        else:
            self.__initial_frame = 0

    def update(self, delta_ms):
        self.do_movement()
        self.do_animation()

    def draw(self, screen: pg.surface.Surface):
        if DEBUG:
            pg.draw.rect(screen, 'red', self.__rect)
        self.__enemy_img = self.__enemy_animation[self.__initial_frame]
        screen.blit(self.__enemy_img, self.__rect)
