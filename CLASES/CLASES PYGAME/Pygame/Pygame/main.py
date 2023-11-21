import pygame as pg

from models.constantes import ALTO_VENTANA, ANCHO_VENTANA, FPS
from models.player.main_player import Jugador

from models.enemy.main_enemy import Enemigo


pg.init()
screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

clock = pg.time.Clock()

back_img = pg.image.load("./assets/img/background/goku_house.png")
back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA))


juego_ejecutandose = True

vegeta = Jugador(0, 0, frame_rate=70, speed_walk=20, speed_run=40)
enemy = Enemigo(0, 400, speed=2)  # Ajusta la velocidad según sea necesario


while juego_ejecutandose:
    lista_eventos = pg.event.get()
    for event in lista_eventos:
        match event.type:
            case pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    vegeta.jump(True)
            case pg.QUIT:
                print("Estoy CERRANDO el JUEGO")
                juego_ejecutandose = False
                break

    lista_teclas_presionadas = pg.key.get_pressed()
    if lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.walk("Right")
    if lista_teclas_presionadas[pg.K_LEFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        vegeta.walk("Left")
    if (
        not lista_teclas_presionadas[pg.K_RIGHT]
        and not lista_teclas_presionadas[pg.K_LEFT]
    ):
        vegeta.stay()

    if (
        lista_teclas_presionadas[pg.K_RIGHT]
        and lista_teclas_presionadas[pg.K_LSHIFT]
        and not lista_teclas_presionadas[pg.K_LEFT]
    ):
        vegeta.run("Right")
    if (
        lista_teclas_presionadas[pg.K_LEFT]
        and lista_teclas_presionadas[pg.K_LSHIFT]
        and not lista_teclas_presionadas[pg.K_RIGHT]
    ):
        vegeta.run("Left")

    delta_ms = clock.tick(FPS)  # Calcula delta_ms aquí
    screen.blit(back_img, back_img.get_rect())
    vegeta.update(delta_ms)
    vegeta.draw(screen)
    enemy.update(delta_ms)
    enemy.draw(screen)
    pg.display.update()

pg.quit()
