import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
    def __init__(self, sets, screen):
        super(Ball, self).__init__()
        self.image = sets.ball_image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.number = sets.ball_number

        self.rect_width = self.rect.width
        self.rect_height = self.rect.height

        # 初始位置
        distant_x = randint(-4, 4) * self.rect_width
        self.rect.x = self.screen_rect.centerx + distant_x
        self.rect.y = 0

    def print_ball(self):
        self.screen.blit(self.image, self.rect)

    def drop_ball(self, sets):
        self.rect.y += sets.ball_speed

    def change_ball(self, sets):
        distant_x = randint(-4, 4) * self.rect_width
        self.rect.x = self.screen_rect.centerx + distant_x
        self.rect.y = 0
