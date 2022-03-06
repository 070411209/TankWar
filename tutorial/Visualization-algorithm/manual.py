#!/usr/bin/python3
import pygame
from random import randint
import random
import sys
from pygame.locals import *

gap = 10  # 竖条的间隔
width = 30  # 竖条的宽度
screenSize = (800, 600)  # 显示屏幕的尺寸
barXPosition = []  # 竖条在坐标轴的位置
Bars = []  # 竖条对象列表

# 生成颜色
class color(object):
    @staticmethod
    def RandomColor():
        r, g, b = randint(0, 225), randint(0, 255), randint(0, 255)
        return (r, g, b)

    @staticmethod
    def CalculateColor(self, num):
        pass


class bar(object):
    def __init__(self, n, num, screen, width=30):
        self.n = n
        self.flag = False
        self.locationX = barXPosition[n]
        self.locationY = screenSize[1]-50-num
        self.num = num
        self.color = color.RandomColor()
        self.width = width
        self.font = pygame.font.Font(None, 20)
        self.screen = screen       
        # self.txt = self.font.render("{}".format(0), True, (0,0,0))
        # self.screen.blit(self.txt, (65, screenSize[1]-40))

    # 绘制竖条及其上方的数字
    def BarDraw(self):
        pygame.draw.rect(self.screen, self.color,
                         ((self.locationX, self.locationY), (self.width, self.num)))
        self.txt = self.font.render("{}".format(self.num), True, self.color)
        self.screen.blit(self.txt, (self.locationX+5, self.locationY-20))

        # self.txt1 = self.font.render("{}".format(self.n), True, (0,0,0))
        # self.screen.blit(self.txt1, (self.locationX+5, screenSize[1]-40))

    def StartPosition(self, idx):
        self.txt = self.font.render("{}".format(idx), True, (0,0,0))
        self.screen.blit(self.txt, (65, screenSize[1]-40))
       

    # 移动竖条，flag是用于判断移动方向 True向右 False向左
    def move(self, flag):
        pace = 2  # 移动的步长
        # 消除移动前的竖条
        pygame.draw.rect(self.screen, (255, 255, 235),
                         ((self.locationX, self.locationY), (self.width, self.num)))
        if flag:
            self.locationX += pace
        else:
            self.locationX -= pace
        # 绘制移动后的竖条
        pygame.draw.rect(self.screen, self.color,
                         ((self.locationX, self.locationY), (self.width, self.num)))

    @staticmethod
    def move_left():
        print("move left")
        return True

    @staticmethod
    def move_right():
        print("move right")
        return False

    @staticmethod
    def change_position():
        print("change")
        return True

     
    def ShowLocation(self, flag):
        # 清除当前位置图像与文字
        pygame.draw.rect(self.screen, (255, 255, 235),
                         ((self.locationX - self.width - 12, screenSize[1]- 45), ((self.width+10)*3, 30))) 
        # if flag == 1:
        #     self.txt = self.font.render("{}".format(self.n), True, (0,0,0))
        #     self.screen.blit(self.txt, (self.locationX-2+5, screenSize[1]-40))

        # if flag == -1:
        #     self.txt = self.font.render("{}".format(self.n), True, (0,0,0))
        #     self.screen.blit(self.txt, (self.locationX+2+5, screenSize[1]-40))

        self.txt1 = self.font.render("{}".format(self.n), True, (0,0,0))
        self.screen.blit(self.txt1, (self.locationX+5, screenSize[1]-40))

        pygame.display.flip()
        pygame.time.delay(100)  # 此延时控制排序动画的快慢

    # 交换相邻两个竖条
    def ChangeLocation(self, otherBall):
        # 清除当前位置图像与文字
        pygame.draw.rect(self.screen, (255, 255, 235),
                         ((self.locationX, self.locationY-20), (self.width, self.num+20)))
        pygame.draw.rect(otherBall.screen, (255, 255, 235),
                         ((otherBall.locationX, otherBall.locationY - 20), (otherBall.width, otherBall.num + 20)))
        # 竖条移动的动画
        for n in range(20):
            self.move(True)
            otherBall.move(False)
            pygame.time.delay(40)
            pygame.display.flip()

        # 移动后，重新写上竖条对应的数字
        self.screen.blit(self.txt, (self.locationX + 5, self.locationY - 20))
        otherBall.screen.blit(
            otherBall.txt, (otherBall.locationX + 5, otherBall.locationY - 20))

        # 交换竖条对象在列表的位置，同时交换排位数字
        Bars[self.n], Bars[otherBall.n] = Bars[otherBall.n], Bars[self.n]
        self.n, otherBall.n = otherBall.n, self.n
        pygame.display.flip()
        pygame.time.delay(100)  # 此延时控制排序动画的快慢

# 冒泡排序
def algorithm(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                Bars[j].ChangeLocation(Bars[j + 1])
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

# 计算十二个竖条在轴上的位置
def barX(gap, width, barXs):
    for n in range(12):
        barX = 50 + gap + (gap + width) * n
        barXs.append(barX)
      
def __game_over():
    pygame.quit()
    exit()

def __check_keydown(event):
    """检查按下按钮的事件"""
    if event.key == pygame.K_LEFT:
        # 按下左键
        hero_direction = -1
    elif event.key == pygame.K_RIGHT:
        # 按下右键
        hero_direction = 1
    elif event.key == pygame.K_SPACE:
        # 坦克发子弹
        hero_direction = 0
    return hero_direction

def __check_keyup(event):
    """检查松开按钮的事件"""
    if event.key == pygame.K_LEFT:
        # 松开左键
        hero_direction = 2
    elif event.key == pygame.K_RIGHT:
        # 松开右键
        hero_direction = 2
    elif event.key == pygame.K_SPACE:
        # 松开上键
        hero_direction = 2
    return hero_direction

def event_handler(idx):
    ret = 2
    for event in pygame.event.get():
        # 判断是否是退出游戏
        if event.type == pygame.QUIT:
            __game_over()
        elif event.type == pygame.KEYDOWN:
            ret = __check_keydown(event)
        elif event.type == pygame.KEYUP:
            ret = __check_keyup(event)

    return ret

def main():
    nums = []
    pygame.init()
    idx = 0
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("少儿编程游戏")  # 标题
    screen.fill((255, 255, 235))  # 背景色
    barX(gap, width, barXPosition)  # 计算bar位置并存于barXs
    # 绘制坐标轴
    pygame.draw.aaline(screen, (0, 0, 0), (50, screenSize[1]-50),
                       (screenSize[0]-50, screenSize[1]-50))  # 绘制坐标轴
    pygame.draw.aaline(screen, (0, 0, 0), (50, screenSize[1]-50),
                       (50, screenSize[1]-200))  # 绘制坐标轴
    pygame.display.flip()
    # 生成十二个竖条并绘制
    L1 = random.sample(range(50, 200), 12)
    print("L1: \n", L1)
    for n in range(12):
        num = randint(1, 20)
        tempBar = bar(n, L1[n], screen)
        tempBar.BarDraw()
        nums.append(L1[n])
        Bars.append(tempBar)
        pygame.time.delay(10)  # 此处延时是为了开始时演示动画效果
        pygame.display.flip()

    # algorithm(nums)  # 排序
    tempBar1 = bar(0, L1[0], screen)
    tempBar1.StartPosition(0)
    pygame.time.delay(10)  # 此处延时是为了开始时演示动画效果
    pygame.display.flip()    
    # 等待关闭窗口事件
    while True:
        ret1 = event_handler(idx)
        if ret1 == 1:
            idx = idx + 1
            if idx >= 0 and idx <= 11:
                Bars[idx].ShowLocation(ret1)
        if ret1 == -1:
            idx = idx - 1
            if idx >= 0 and idx <= 11: 
                Bars[idx].ShowLocation(ret1)
        if ret1 == 0:
            if idx >= 0 and idx < 11:
                Bars[idx].ChangeLocation(Bars[idx + 1])
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]              
        pygame.display.update()
        pygame.time.Clock().tick(300)
        
if __name__ == "__main__":
    main()
