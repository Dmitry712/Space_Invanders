import pygame

class Ino(pygame.sprite.Sprite):
    """Класс одного пришельца или сразу нескольких прищельцев"""
    def __init__(self, screen):
        """Инициализируем и задаем начальную позицию своим пришельца"""
        super(Ino, self). __init__()

        #так как класс дочерний используем  команду super
        self.screen = screen #сам экран там где мы все отрисовываем
        self.image = pygame.image.load('../images/ino.png') #изображение прищельца на экране с помощью приложения PixelArt
        self.rect = self.image.get_rect() #расположение пришельца
        self.rect.x = self.rect.width #выравнивание прищельцов в левую верхнюю часть экрана и ширину нашего изображения
        self.rect.y = self.rect.height # выоста нашего изображения
        self.x =float(self.rect.x) # преобразуем в вешественное число в тип float чтобы двигалось все плавно
        self.y = float(self.rect.y) # тут тоже самое
        self.shag = 0.5

    def reverse_move(self):
        self.shag = -self.shag

    def a_move(self):
        self.shag *= 2

    def draw(self): #движение
        """Вывод пришельца на главный экран и его движения  """
        self.screen.blit(self.image, self.rect) # отрисовываем наших пришельцев с помощью команды blit

    def update(self):
        screen_rect = self.screen.get_rect()
        for group in self.groups():
            for ino in group.sprites():
                if ino.rect.right >= screen_rect.right or ino.rect.left <= screen_rect.left:
                    self.reverse_move()
                    break
        """Перемещает пришельцев по экрану"""
        self.y += 0.1
        self.rect.y = self.y # перемещает вниз
        self.x += self.shag
        self.rect.x = self.x



