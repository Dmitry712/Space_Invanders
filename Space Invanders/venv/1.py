import pygame, Controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores



def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Invanders 2")
    bg_color = (0, 0, 0)
    gun = Gun(screen) #отрисовываем пушку в игре
    bullets = Group()#обьект
    inos = Group()#обьект
    Controls.create_army(screen,inos) # вывод армии на главный экран
    stats = Stats() #рекорды
    sc = Scores(screen, stats)

    while True:
        Controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            Controls.update(bg_color, screen, stats, sc, gun, inos,  bullets)
            Controls.update_bullets(screen, stats, sc, inos, bullets)
            Controls.update_inos(stats, screen, sc, gun, inos, bullets)


run()



