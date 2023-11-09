from models.auxiliar import SurfaceManager as sf
import pygame as pg
from models.constantes import ANCHO_VENTANA, DEBUG, ALTO_VENTANA


class Jugador:

    def __init__(self, coord_x, coord_y, frame_rate = 100, speed_walk = 6, speed_run = 12, gravity = 16, jump = 32):
        self.__iddle_r = sf.get_surface_from_spritesheet('./assets/img/player/iddle/player_idle.png', 5, 1)
        self.__iddle_l = sf.get_surface_from_spritesheet('./assets/img/player/iddle/player_idle.png', 5, 1, flip=True)
        self.__walk_r = sf.get_surface_from_spritesheet('./assets/img/player/walk/player_walk.png', 6, 1)
        self.__walk_l = sf.get_surface_from_spritesheet('./assets/img/player/walk/player_walk.png', 6, 1, flip=True)
        self.__run_r = sf.get_surface_from_spritesheet('./assets/img/player/run/player_run.png', 2, 1)
        self.__run_l = sf.get_surface_from_spritesheet('./assets/img/player/run/player_run.png', 2, 1, flip=True)
        self.__jump_r = sf.get_surface_from_spritesheet('./assets/img/player/jump/player_jump.png', 6, 1)
        self.__jump_l = sf.get_surface_from_spritesheet('./assets/img/player/jump/player_jump.png', 6, 1, flip=True)
        self.__move_x = coord_x
        self.__move_y = coord_y
        self.__speed_walk = speed_walk
        self.__speed_run = speed_run
        self.__frame_rate = frame_rate
        self.__player_move_time = 0
        self.__player_animation_time = 0
        self.__gravity = gravity
        self.__jump = jump
        self.__is_jumping = False
        self.__initial_frame = 0
        self.__actual_animation = self.__iddle_r
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        self.__rect = self.__actual_img_animation.get_rect()
        self.__is_looking_right = True

    
    def __set_x_animations_preset(self, move_x, animation_list: list[pg.surface.Surface], look_r: bool):
        self.__move_x = move_x
        self.__actual_animation = animation_list
        self.__is_looking_right = look_r
        
    
    def __set_y_animations_preset(self):
        self.__move_y = -self.__jump
        self.__move_x = self.__speed_run if self.__is_looking_right else -self.__speed_run
        self.__actual_animation = self.__jump_r if self.__is_looking_right else self.__jump_l
        self.__initial_frame = 0
        self.__is_jumping = True
    
    def walk(self, direction: str = 'Right'):
        match direction:
            case 'Right':
                look_right = True
                self.__set_x_animations_preset(self.__speed_walk, self.__walk_r, look_r=look_right)
            case 'Left':
                look_right = False
                self.__set_x_animations_preset(-self.__speed_walk, self.__walk_l, look_r=look_right)
    
    def run(self, direction: str = 'Right'):
        self.__initial_frame = 0
        match direction:
            case 'Right':
                look_right = True
                self.__set_x_animations_preset(self.__speed_run, self.__run_r, look_r=look_right)
            case 'Left':
                look_right = False
                self.__set_x_animations_preset(-self.__speed_run, self.__run_l, look_r=look_right)
    
    def stay(self):
        if self.__actual_animation != self.__iddle_l and self.__actual_animation != self.__iddle_r:
            self.__actual_animation = self.__iddle_r if self.__is_looking_right else self.__iddle_l
            self.__initial_frame = 0
            self.__move_x = 0
            self.__move_y = 0
    
    def jump(self, jumping=True):
        if jumping and not self.__is_jumping:
            self.__set_y_animations_preset()
        else:
            self.__is_jumping = False
            self.stay()
    
    def __set_borders_limits(self):
        pixels_move = 0
        if self.__move_x > 0:
            pixels_move = self.__move_x if self.__rect.x < ANCHO_VENTANA - self.__actual_img_animation.get_width() else 0
        elif self.__move_x < 0:
            pixels_move = self.__move_x if self.__rect.x > 0 else 0
        return pixels_move


    def do_movement(self, delta_ms):
        self.__player_move_time += delta_ms
        if self.__player_move_time >= self.__frame_rate:
            self.__player_move_time = 0
            self.__rect.x += self.__set_borders_limits()
            self.__rect.y += self.__move_y
            # Parte relacionado a saltar
            if self.__rect.y < 300:
                self.__rect.y += self.__gravity

    def do_animation(self, delta_ms):
        self.__player_animation_time += delta_ms
        if self.__player_animation_time >= self.__frame_rate:
            self.__player_animation_time = 0
            if self.__initial_frame < len(self.__actual_animation) - 1:
                self.__initial_frame += 1
            else:
                self.__initial_frame = 0
                # if self.__is_jumping:
                #     self.__is_jumping = False
                #     self.__move_y = 0
    
    def update(self, delta_ms):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
    
    def draw(self, screen: pg.surface.Surface):
        if DEBUG:
            pg.draw.rect(screen, 'red', self.__rect)
            #pg.draw.rect(screen, 'green', self.__rect.bottom)
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        screen.blit(self.__actual_img_animation, self.__rect)