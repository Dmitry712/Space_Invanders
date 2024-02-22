import pygame, sys
from bullet import bullet
from ino import Ino
import time

def events(screen, gun, bullets):
    """обработка событий происходящих на экране"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:#нажатая клавиша
            #кнопка вправо
            if event.key == pygame.K_d:
                #указание клавиши куда оно будет двигаться сделал на буквы WASD можно сделать по другому на стрелки сделая тоже самое
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                # стрельба из пушки
                new_bullet = bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP: # клавиша отжата если палец убрал с кнопки то он не будет двигаться
            #вправо
            if event.key == pygame.K_d:
                gun.mright = False
                #движение влево
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, stats, sc, gun, inos, bullets):
    """Обновление экрана при запуске игры"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen) #этот метод используется для рисовки
    pygame.display.flip()

def update_bullets(screen, stats, sc, inos, bullets):
    """Обновление позиции пуль на экране"""
    bullets.update() # перемещаем
    # мы делаем что после предела экрана пули исчезнут чтобы не занимать много памяти и делаем проверку чтобы все сработала как было задумано
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            #print(len(bullets))  это проверка пуль на исчезновение
    collisions = pygame.sprite.groupcollide(bullets, inos, True,True)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:
        bullets.empty()
        inos = create_army(screen, inos)
        for i in inos:
            i.a_move()

def gun_kill(stats, screen, sc, gun, inos, bullets):
    """столкновение пушки и прищельцев"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(5)
    else:
        stats.run_game = False
        sys.exit()
def update_inos(stats, screen, sc, gun, inos, bullets):
    """обновляет позицию иноприщеленцов"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)
def inos_check(stats, screen, sc, gun, inos, bullets):
    """проверка, добралась ли армия до края экрана"""
    pass
    # screen_rect = screen.get_rect()
    # for ino in inos.sprites():
    #     if ino.rect.right >= screen_rect.right:
    #         break
    # else:
    #     return
    # for ino in inos.sprites():
    #     ino.reverse_move()
    #         # for ino in inos.sprites():
    #         #     if ino.rect.right_wall >= screen_rect.right_wall:
    #         #         gun_kill(stats, screen, sc, gun, inos, bullets)
    #         #         break
def create_army(screen, inos):
    """Создание армии пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 1 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)
    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x - 1):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height *row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)
    return inos


def check_high_score(stats, sc):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            #открываем файл для рекордов
            f.write(str(stats.high_score))







