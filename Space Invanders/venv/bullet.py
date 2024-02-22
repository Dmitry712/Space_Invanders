import pygame

class bullet(pygame.sprite.Sprite): #спрайт это обьект на экране который может двигаться
    #дочерний класс

    def __init__(self, screen, gun):
        """создаем позиции пушки для игры """
        super(bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 8)
        #откуда будут вылетать пули и ее размер
        self.color = 237, 28, 36 #координаты цвета
        """Цвет пуль из пушки"""
        self.speed = 5
        """Скорость пушки"""
        self.rect.centerx = gun.rect.centerx
        """Расположение пушки на экране"""
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed
        """скорость полета пули"""
        self.rect.y = self.y
        """расположение пуль"""
    def draw_bullet(self):
        """рисуем пулю на экране и ее детализация с цветом"""
        pygame.draw.rect(self.screen, self.color, self.rect)
