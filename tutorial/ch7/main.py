# -*- coding: utf-8 -*-

"""
   奥特曼打怪兽射击游戏,本程序需要pygame的混音器支持,所以需要安装pygame模块才能正常运行。
   游戏操作方法：用鼠标指针牵引奥特曼，单击左键射击，碰到怪兽奥特曼死亡，杀死100个游戏成功结束。
"""

import imp
import pygame
import os
from pygame import Rect
from settings import *
import random



class BaseSprite(pygame.sprite.Sprite):
    """
    BaseSprite类，游戏中所有变化物体的底层父类
    """
    def __init__(self, image_name, screen):
        super().__init__()
        self.screen = screen
        self.direction = None
        self.speed = None
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()

    def update(self):
        self.speed = 1



class TankSprite(BaseSprite):
    """
    ImageSprite类，BaseSprite的子类，所有带图片的精灵的父类
    """
    def __init__(self, image_name, screen):
        super().__init__(image_name, screen)
        self.is_alive = True
        self.is_moving = False


    def update(self):
        if not self.is_alive:
            return
        super(TankSprite, self).update()
        


class Enemy(TankSprite):

    def __init__(self, image_name, screen):
        super().__init__(image_name, screen)
        self.is_hit_wall = False


    def update(self):
        super().update()



class Hero(TankSprite):

    def __init__(self, image_name, screen):
        super(Hero, self).__init__(image_name, screen)
        self.type = HERO
        self.speed = HERO_SPEED
        self.direction = UP
        self.is_hit_wall = False
        # 初始化英雄的位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.top = 0 #SCREEN_RECT.centerx

    def update(self):
        if not self.is_hit_wall:
            super().update()

class TankWar:

    def __init__(self):
               
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.bg_color = (0, 0, 0)
        self.hero = None
        self.enemies = None

    def __init_game(self):
        """
        初始化游戏的一些设置
        :return:
        """
        pygame.init()   # 初始化pygame模块
        pygame.display.set_caption("我是奥特曼")  # 设置窗口标题
        pygame.mixer.init()    # 初始化音频模块

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否是退出游戏
            if event.type == pygame.QUIT:
                TankWar.__game_over()

    def __create_sprite(self):
        self.hero = Hero(HERO_IMAGE_NAME, self.screen)
        self.enemies = pygame.sprite.Group()
        for i in range(ENEMY_COUNT):
            direction = random.randint(0, 3)
            enemy = Enemy(ENEMY_IMAGES[direction], self.screen)
            enemy.direction = direction
            self.enemies.add(enemy)

    def __update_sprites(self):
        self.hero.update()
        self.screen.blit(self.hero.image, self.hero.rect)
        self.enemies.update()
        self.enemies.draw(self.screen)

    def run_game(self):
        self.__init_game()
        self.__create_sprite()
        
        while True:
            self.__event_handler()
            self.screen.fill(self.bg_color)
            self.__update_sprites()
            # 5、更新显示
            pygame.display.update()
            pygame.time.Clock().tick(60)            


    @staticmethod
    def __game_over():
        pygame.quit()
        exit()

def main():
    tankWar = TankWar()
    tankWar.run_game()

if __name__ == '__main__':
    main()

