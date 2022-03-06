import os
from pygame import Rect



HERO_IMAGE_NAME = "h1.png"
SCREEN_RECT = Rect(0, 0, 800, 600)  # 屏幕矩形 

HERO = 0

# 通用变量
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

HERO_SPEED = 2

ENEMY_COUNT = 2

ENEMY_IMAGES = {
    LEFT: "h2.png",
    RIGHT: "h2.png",
    UP: "h2.png",
    DOWN: "h2.png"
}
