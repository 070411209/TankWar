# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
# @Time    : 2021.12
# @Author  : 高二水令
# @Software: 图层拖拽缩放
import os
import sys
import pygame
from pygame.locals import *


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
# 写一个函数，判断一个点是否在某个范围内
# 点（x,y）
# 范围 rect(x,y,w,h)


def is_in_rect(pos, rect):
    x, y = pos
    rx, ry, rw, rh = rect
    if (rx <= x <= rx+rw) and (ry <= y <= ry+rh):
        return True
    return False


def move_image(pic_bottom, pic_upper):
    # pic_bottom,pic_upper分别是背景图和上层拖拽图层，ssn是我自己设置的路径信息、不需要可以删去、需要直接运行可以改成main()
    pygame.init()
    screen = pygame.display.set_mode((710, 520))
    BackGround = Background(pic_bottom, [0, 0])
    screen.fill((255, 255, 255))
    myimage = pygame.image.load('.\\next.png')
    myimage = pygame.transform.scale(myimage, (90, 40))
    myimage_x = 600
    myimage_y = 480
    scale_ = pygame.image.load('.\\Avel_scale.tif')
    scale_ = pygame.transform.scale(scale_, (70, 520))
    scale_x = 632
    scale_y = 0
    screen.blit(BackGround.image, BackGround.rect)
    screen.blit(scale_, (scale_x, scale_y))
    screen.blit(myimage, (myimage_x, myimage_y))
    pygame.display.set_caption('图像定标')
    size = []
    location = [0, 0]

    image = pygame.image.load(pic_upper)
    image_x = 100
    image_y = 100
    screen.blit(image, (image_x, image_y))
    pygame.display.flip()

    is_move = False
    run_flag = True
    while (run_flag == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # 鼠标按下、让状态变成可以移动
            if event.type == pygame.MOUSEBUTTONDOWN:
                w, h = image.get_size()
                if is_in_rect(event.pos, (image_x, image_y, w, h)):
                    is_move = True

            # 鼠标弹起、让状态变成不可以移动
            if event.type == pygame.MOUSEBUTTONUP:
                is_move = False

            # 鼠标移动对应的事件
            if event.type == pygame.MOUSEMOTION:
                if is_move:
                    screen.fill((255, 255, 255))
                    screen.blit(BackGround.image, BackGround.rect)
                    x, y = event.pos
                    image_w, image_h = image.get_size()
                    # 保证鼠标在图片的中心
                    image_y = y-image_h/2
                    image_x = x-image_w/2
                    screen.blit(scale_, (scale_x, scale_y))
                    screen.blit(myimage, (myimage_x, myimage_y))
                    screen.blit(image, (image_x, image_y))
                    # print(image.get_rect())
                    location[0] = event.pos[0]
                    location[1] = event.pos[1]
                    print(event.pos)
                    pygame.display.update()
                    # 鼠标按钮响应、是点击图片的位置范围进行跳转
            if event.type == pygame.MOUSEBUTTONDOWN and myimage_x <= event.pos[0] <= myimage_x + 90 and \
                    myimage_y <= event.pos[1] <= myimage_y + 40:  # 判断鼠标位置以及是否摁了下去
                # 这里可以写按钮响应的功能

                pygame.quit()  # 关闭原来窗口
                # os.system('ui.py')
                run_flag = False  # 跳出循环(不然会报错)
                # sys.exit()
         # 滚轮缩放
            if event.type == MOUSEWHEEL:
                screen.fill((255, 255, 255))
                screen.blit(BackGround.image, BackGround.rect)
                image_width = image.get_width()
                image_heigt = image.get_height()
                image = pygame.transform.scale(image, (
                    image_width + event.y * image_width / image_heigt * 10, image_heigt + event.y * 10))
                screen.blit(scale_, (scale_x, scale_y))
                screen.blit(myimage, (myimage_x, myimage_y))
                screen.blit(image, (image_x, image_y))
                # print(event)
                print(image_width, image_heigt)
                # print(event.flipped)
                pygame.display.update()

if __name__ == '__main__':
    pic_bottom = ""
    pic_upper = ""
    move_image(pic_bottom, pic_upper)
