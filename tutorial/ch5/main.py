import pygame
import sys
from pygame.locals import *
import random


class Monkey(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        # position = 300, 710
        self.speed = [0, 0]
        self.img = pygame.image.load('b.png')
        self.rect = self.img.get_rect()
        self.rect.center = position
        self.image = self.img

    def move_left(self):
        self.speed = [-6, 0]
        if self.rect.left < 0:
            self.rect.left = 0
        else:
            self.rect = self.rect.move(self.speed)

    def move_right(self):
        self.speed = [6, 0]
        if self.rect.right > 600:
            self.rect.right = 600
        else:
            self.rect = self.rect.move(self.speed)

    def move_up(self):
        self.speed = [0, -6]
        if self.rect.top < 0:
            self.rect.top = 0
        else:
            self.rect = self.rect.move(self.speed)

    def move_down(self):
        self.speed = [0, 6]
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
        self.img = pygame.image.load('a.png')
        self.rect = self.img.get_rect()
        self.rect.center = position
        self.image = self.img
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)


class Letter(pygame.sprite.Sprite):
    def __init__(self, data):
        pygame.sprite.Sprite.__init__(self)
        x = random.randint(10, 500)
        position = [x, 20]
        speed = [0, 3]

        # 创建字体对象
        self.font = pygame.font.Font(None, 200)
        # 文本与颜色
        self.text = self.font.render(data, 1, (75, 0, 130))
        # 获取设置后新的坐标区域
        self.textpos = self.text.get_rect(center=position)
        self.rect = self.text.get_rect()
        self.rect.center = position
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)


def main():
    pygame.init()
    white = (255, 255, 255)
    charachter = []
    for i in range(1, 100, 1):
        charachter.append(str(i))

    # charachter = ["Aa", "Bb", "Cc", "Dd", "Ee", "Ff", "Gg", "Hh", "Ii", "Jj", "Kk", "Ll", "Mm", "Nn", "Oo",
    #               "Pp", "Qq", "Rr", "Ss", "Tt", "Uu", "Vv", "Ww", "Xx", "Yy", "Zz", ""]
    size = width, height = 600, 800
    screen = pygame.display.set_mode(size)
    font = pygame.font.Font(None, 120)
    text = font.render("PENG!", 1, (0, 255, 0))

    # bg = pygame.image.load('background.jpg')
    pygame.display.set_caption("少儿英语编程")
    group = pygame.sprite.Group()
    # 获取中心的坐标
    center = (screen.get_width()/2, screen.get_height()/2)
    textpos = text.get_rect(center=center)
    mk = Monkey(center)
    i = 0
    j = 0
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

        screen.fill(white)
        screen.blit(mk.image, mk.rect)

        if i % 300 == 0:
            if j < 26:
                lt = Letter(charachter[j])
                group.add(lt)
            j = j + 1
        i = i + 1
        for b in group.sprites():
            b.move()
            screen.blit(b.text, b.rect)
            # b = pygame.sprite.collide_rect_ratio(0.9)(mk, b)  #两个精灵之间的矩形碰撞检测
            ret = pygame.sprite.collide_rect(mk, b)
            if ret:
                screen.blit(text, textpos)
        pygame.display.update()
        pygame.time.Clock().tick(60)


if __name__ == '__main__':
    main()
