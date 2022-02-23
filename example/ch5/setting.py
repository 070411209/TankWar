import pygame

class Settings():
    def __init__(self):
        self.gameover = True # 游戏结束标志
        self.catch_number = 0 # 接住的球数目

        self.bg_width = 800
        self.bg_height = 600
        self.bg_color = (255, 255, 255)

        self.ball_image = pygame.image.load('ball.png')
        self.ball_speed = 1
        self.ball_number = 3 # 球的数量

        self.bowl_image = pygame.image.load('wan.png')
        self.bowl_speed = 10

        self.button_width = 200
        self.button_height = 50
        self.button_bg_color = (0, 0, 0)
        self.button_word_color = (200, 0, 0)
