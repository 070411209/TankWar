import pygame
from random import randint

# 初始化程序
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("c语言中文网")
# 更新显示
pygame.display.flip()

flag = False
while True:
    #等待事件发生
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit("成功退出")

    if event.type == pygame.MOUSEBUTTONDOWN:
        print('鼠标按下')
        flag = True
    if event.type == pygame.MOUSEBUTTONUP:
        print('鼠标弹起')
        flag = False
        pass

    if event.type == pygame.MOUSEMOTION and flag == True:
        # 随机生成 RGB 颜色值
        color = (randint(0, 255), randint(0, 255), randint(0, 255))  # 颜色随机   
        # pos 获取鼠标当前位置
        print('鼠标移动',event.pos)
        mx,my = event.pos
        # 调用 pygame.draw 模块画圆
        pygame.draw.circle(screen, color, (mx, my), 50)
        # 处理完，更新显示
        pygame.display.update()