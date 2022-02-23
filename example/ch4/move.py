# -*- coding=utf-8 -*-
import pygame
from pygame.locals import KEYDOWN
import random

w, h = 800, 600
pygame.init()
screen = pygame.display.set_mode((w, h))

white = 255, 255, 255
black = 0, 0, 0
# myfont = pygame.font.Font(None, 80)
myfont = pygame.font.SysFont("arial",60)



word_diff_ticks = 1000
word_ticks = pygame.time.get_ticks() + word_diff_ticks


def get_random_word():
    color = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))  # 颜色随机
    x = random.randint(100, w-100)  # x坐标从左右边距各100之间随机
    y = 0
    word = random.randint(65, 90)
    return x, y, word, color


arr = []
arr.append(get_random_word())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    for i in range(len(arr)):  # 绘制这些字母
        x, y, word, c = arr[i]
        textImage = myfont.render(chr(word), True, c)
        screen.blit(textImage, (x, y))

    if pygame.time.get_ticks() >= word_ticks:  # 计时增加新字母
        word_ticks += word_diff_ticks
    
    arr.append(get_random_word())

    pygame.display.update()
