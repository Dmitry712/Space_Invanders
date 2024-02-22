import pygame
from pygame.sprite import Sprite

class Gun(Sprite):

    def __init__(self, screen):
        """инициализация пушки"""
        super(Gun, self). __init__()
        self.screen = screen
        self.image = pygame.image.load('../images/Gun.png')
        #передаем пайгейму саму пушку и выводи на экран(screen)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #обьект нашего экрана
        self.rect.centerx = self.screen_rect.centerx
        #по центру пушка
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        #координаты пушки
        self.mright = False
        self.mleft = False

    def output(self):
        """рисование пушки на экране"""
        self.screen.blit(self.image, self.rect)
        #рисование нашей пушки на экране метод блит отрисовывает как раз нашу пушку
    def update_gun(self):
        """Обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            #движение пушки вправо и при столкновении с границей он остановится и дальше вправо не пойдет
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            #движение пушки в лево
            self.center -= 1.5

        self.rect.centerx= self.center

    def create_gun(self):
        """размещает пушку по центру внизу на главном экране"""
        self.center = self.screen_rect.centerx





