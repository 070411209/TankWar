import pygame
import sys
from pygame.locals import *
import random


class Monkey(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        # position = 300, 710
        self.speed = [0, 0]
        self.img = pygame.image.load('monkey.png')
        self.rect = self.img.get_rect()
        self.rect.center = position
        self.image = self.img

    def move_left(self):
        self.speed = [-5, 0]
        if self.rect.left < 0:
            self.rect.left = 0
        else:
            self.rect = self.rect.move(self.speed)

    def move_right(self):
        self.speed = [5, 0]
        if self.rect.right > 600:
            self.rect.right = 600
        else:
            self.rect = self.rect.move(self.speed)

    def move_up(self):
        self.speed = [0, -5]
        if self.rect.top < 0:
            self.rect.top = 0
        else:
            self.rect = self.rect.move(self.speed)

    def move_down(self):
        self.speed = [0, 5]
        if self.rect.bottom > 800:
            self.rect.bottom = 800
        else:
            self.rect = self.rect.move(self.speed)


class Banana(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        x = random.randint(20, 580)
        position = [x, 20]
        speed = [0, 3]
        self.img = pygame.image.load('banana.png')
        self.rect = self.img.get_rect()
        self.rect.center = position
        self.image = self.img
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)


def main():
    pygame.init()
    white = (0, 0, 0)
    size = width, height = 600, 800
    font = pygame.font.Font(None, 56)
    screen = pygame.display.set_mode(size)
    text = font.render("Peng Peng Peng", 1, (255, 10, 10))
    bg = pygame.image.load('background.jpg')
    pygame.display.set_caption("游戏")
    mk = Monkey([200, 710])
    mk1 = Monkey([500, 710])
    group = pygame.sprite.Group()
    # 获取中心的坐标
    center = (screen.get_width()/2, screen.get_height()/2)
    # 获取设置后新的坐标区域
    textpos = text.get_rect(center=center)

    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            mk.move_left()
        if key[K_RIGHT]:
            mk.move_right()
        if key[K_UP]:
            mk.move_up()
        if key[K_DOWN]:
            mk.move_down()

        # screen.blit(bg, bg.get_rect())
        screen.fill(white)
        screen.blit(mk.image, mk.rect)
        screen.blit(mk1.image, mk1.rect)

        i = i + 1
        if i % 30 == 0:
            ba = Banana()
            group.add(ba)
        for b in group.sprites():
            b.move()
            screen.blit(b.img, b.rect)
            if pygame.sprite.collide_mask(mk, b):  # 碰撞检测
                screen.blit(text, textpos)
        pygame.display.update()
        pygame.time.Clock().tick(60)


if __name__ == '__main__':
    main()
