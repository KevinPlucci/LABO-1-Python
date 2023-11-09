import pygame as pg

from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador

from models.enemy.main_enemy import Enemigo


screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.init()
clock = pg.time.Clock()

back_img = pg.image.load('./assets/img/background/goku_house.png')
back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA))


juego_ejecutandose = True

vegeta = Jugador(0, 0, frame_rate=70, speed_walk=20, speed_run=40)
enemy = Enemigo(ANCHO_VENTANA, ALTO_VENTANA - 100, speed=5)


while juego_ejecutandose:
    
    #print(delta_ms)
    lista_eventos = pg.event.get()
    for event in lista_eventos:
        match event.type:
            case pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    vegeta.jump(True)
            # case pg.KEYUP:
            #     if event.key == pg.K_SPACE:
            #         print('Estoy SOLTANDO el espacio')
            case pg.QUIT:
                print('Estoy CERRANDO el JUEGO')
                juego_ejecutandose = False
                break
    
    lista_teclas_presionadas = pg.key.get_pressed()
    if lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.walk('Right')
    if lista_teclas_presionadas[pg.K_LEFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        vegeta.walk('Left')
    if not lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.stay()
    
    if lista_teclas_presionadas[pg.K_RIGHT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.run('Right')
    if lista_teclas_presionadas[pg.K_LEFT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        vegeta.run('Left')
    
        
    
    screen.blit(back_img, back_img.get_rect())
    delta_ms = clock.tick(FPS)
    vegeta.update(delta_ms)
    vegeta.draw(screen)
    enemy.update(delta_ms)
    enemy.draw(screen)
    pg.display.update()

pg.quit()