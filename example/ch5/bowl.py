import pygame

class Bowl:
    def __init__(self, sets, screen):
        self.image = sets.bowl_image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.moving = 0

        # 初始位置，屏幕底部中间
        self.rect.centerx = sets.bg_width / 2
        self.rect.centery = sets.bg_height - self.rect.height / 2

    def print_bowl(self):
        self.screen.blit(self.image, self.rect)

    def move_bowl(self, sets):
        if self.moving != 0 :
            if self.moving == 1 and self.rect.right < sets.bg_width:
                self.rect.centerx += sets.bowl_speed
            elif self.moving == -1 and self.rect.left > 0:
                self.rect.centerx -= sets.bowl_speed


