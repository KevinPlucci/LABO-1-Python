import pygame
import sys
from models.stage import Stage
from auxiliar.constantes import (screen_h, screen_w)

class Game:

    def __init__(self) -> None:
        pass

    def run_stage(stage_name: str):
        pygame.init()
    
        screen = pygame.display.set_mode((screen_w, screen_h))
        clock = pygame.time.Clock()
        game = Stage(screen, screen_w, screen_h, stage_name)  # instancia de la clase
        #game = Game(screen_w, screen_h, "stage_2")  # instancia de la clase

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill((30, 30, 30))  # relleno fondo
            delta_ms = clock.tick(30)
            game.run(delta_ms)
            pygame.display.flip()
