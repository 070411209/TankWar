# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:51:46 2021

@author: Administrator
"""

import pygame as pg
from pygame.locals import *
import sys
import time

mmap=list()
with open("F:/其它/level_file.txt",'r') as f:
    for line in f.readlines():
        l=line.strip()
        mmap.append(l)

white=(255,255,255)
black=(0,0,0)
man=(50,250,50)
box=(200,200,0)
dest=(100,100,100)

img_man=pg.image.load('F:/images/pig.jpg')
img_box=pg.image.load('F:/images/box.jpg')
img_wall=pg.image.load('F:/images/wall.jpg')
img_dest=pg.image.load('F:/images/dest.png')

pg.init()
screen=pg.display.set_mode((200,200))
pg.display.set_caption("推箱子")

it=0
x,y=0,0
man_pos,box_pos,barrier_pos,dest_pos,space_pos=[],[],[],[],[]
def get_map(mmap,it):
    man_pos,box_pos,barrier_pos,dest_pos,space_pos=[],[],[],[],[]
    for i in range(len(mmap[it])):
        x=(i%10)*20
        y=(i//10)*20
        if mmap[it][i]=='4':
            man_pos.extend((x,y))
        elif mmap[it][i]=='2':
            box_pos.append([x,y])
        elif mmap[it][i]=='1':
            barrier_pos.append([x,y])
        elif mmap[it][i]=='3':
            dest_pos.append([x,y])
        if mmap[it][i]=='0' or mmap[it][i]=='2' or mmap[it][i]=='3' or mmap[it][i]=='4':
            space_pos.append([x,y])
    return [man_pos,box_pos,barrier_pos,dest_pos,space_pos]

last_move=['0']
def move(man_pos,box_pos,barrier_pos,space_pos,last_move):
    for event in pg.event.get():
        if event.type==QUIT:
            pg.quit()
            sys.exit()
        elif event.type==KEYDOWN:
            #人物上移
            if event.key==K_UP and [man_pos[0],man_pos[1]-20] in space_pos:
                if [man_pos[0],man_pos[1]-20] in box_pos:
                    if [man_pos[0],man_pos[1]-40] in space_pos and [man_pos[0],man_pos[1]-40] not in box_pos:
                        for i in range(len(box_pos)):
                            if box_pos[i]==[man_pos[0],man_pos[1]-20]:
                                box_pos[i]=[man_pos[0],man_pos[1]-40]
                        man_pos[1]-=20
                        last_move.append('UP')
                else:
                    man_pos[1]-=20
                    last_move.append('up')
            #人物下移
            elif event.key==K_DOWN and [man_pos[0],man_pos[1]+20] in space_pos:
                if [man_pos[0],man_pos[1]+20] in box_pos:
                    if [man_pos[0],man_pos[1]+40] in space_pos and [man_pos[0],man_pos[1]+40] not in box_pos:
                        for i in range(len(box_pos)):
                            if box_pos[i]==[man_pos[0],man_pos[1]+20]:
                                box_pos[i]=[man_pos[0],man_pos[1]+40]
                        man_pos[1]+=20
                        last_move.append('DOWN')
                else:
                    man_pos[1]+=20
                    last_move.append('down')
            #人物左移
            elif event.key==K_LEFT and [man_pos[0]-20,man_pos[1]] in space_pos:
                if [man_pos[0]-20,man_pos[1]] in box_pos:
                    if [man_pos[0]-40,man_pos[1]] in space_pos and [man_pos[0]-40,man_pos[1]] not in box_pos:
                        for i in range(len(box_pos)):
                            if box_pos[i]==[man_pos[0]-20,man_pos[1]]:
                                box_pos[i]=[man_pos[0]-40,man_pos[1]]
                        man_pos[0]-=20
                        last_move.append('LEFT')
                else:
                    man_pos[0]-=20
                    last_move.append('left')
            #人物右移
            elif event.key==K_RIGHT and [man_pos[0]+20,man_pos[1]] in space_pos:
                if [man_pos[0]+20,man_pos[1]] in box_pos:
                    if [man_pos[0]+40,man_pos[1]] in space_pos and [man_pos[0]+40,man_pos[1]] not in box_pos:
                        for i in range(len(box_pos)):
                            if box_pos[i]==[man_pos[0]+20,man_pos[1]]:
                                box_pos[i]=[man_pos[0]+40,man_pos[1]]
                        man_pos[0]+=20
                        last_move.append('RIGHT')
                else:
                    man_pos[0]+=20
                    last_move.append('right')
            elif event.key==K_KP0:
                print(last_move[-1])
                if last_move[-1]=='UP':
                    last_move.pop()
                    man_pos[1]+=20
                    for i in range(len(box_pos)):
                        if box_pos[i]==[man_pos[0],man_pos[1]-40]:
                            box_pos[i]=[man_pos[0],man_pos[1]-20]
                elif last_move[-1]=='up':
                    last_move.pop()
                    man_pos[1]+=20
                if last_move[-1]=='DOWN':
                    last_move.pop()
                    man_pos[1]-=20
                    for i in range(len(box_pos)):
                        if box_pos[i]==[man_pos[0],man_pos[1]+40]:
                            box_pos[i]=[man_pos[0],man_pos[1]+20]
                elif last_move[-1]=='down':
                    last_move.pop()
                    man_pos[1]-=20
                if last_move[-1]=='LEFT':
                    last_move.pop()
                    man_pos[0]+=20
                    for i in range(len(box_pos)):
                        if box_pos[i]==[man_pos[0]-40,man_pos[1]]:
                            box_pos[i]=[man_pos[0]-20,man_pos[1]]
                elif last_move[-1]=='left':
                    last_move.pop()
                    man_pos[0]+=20
                if last_move[-1]=='RIGHT':
                    last_move.pop()
                    man_pos[0]-=20
                    for i in range(len(box_pos)):
                        if box_pos[i]==[man_pos[0]+40,man_pos[1]]:
                            box_pos[i]=[man_pos[0]+20,man_pos[1]]
                elif last_move[-1]=='right':
                    last_move.pop()
                    man_pos[0]-=20
                

def game_pass(screen,box_pos,dest_pos):
    not_over=0
    for i in box_pos:
        if i not in dest_pos:
            not_over=1
            break
    if not_over==0:
        return 1

def next_task():
    pg.font.init()
    fontObj=pg.font.SysFont('SimHei', 15)
    textSurfaceObj=fontObj.render('下一关', True, white,black)
    textRectObj=textSurfaceObj.get_rect()
    textRectObj.center=(150,150)
    screen.blit(textSurfaceObj, textRectObj)
    pg.display.update()
    for event in pg.event.get():
        if event.type==QUIT:
            pg.quit()
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            pos=pg.mouse.get_pos()
            if 125<=pos[0]<=175 and 125<=pos[1]<175:
                return 1
        elif event.type==KEYDOWN:
            if event.key==K_RETURN:
                return 1
    return 0

def draw_flip(screen,man_pos,box_pos,barrier_pos,dest_pos):
    for i in dest_pos:
        screen.blit(img_dest,(i[0],i[1]))
    for i in barrier_pos:
        screen.blit(img_wall,(i[0],i[1]))
    for i in box_pos:
        screen.blit(img_box,(i[0],i[1]))
    screen.blit(img_man,(man_pos[0],man_pos[1]))

it=0
def main(screen,it,mmap,man_pos,barrier_pos,box_pos,dest_pos):
    while True:
        #fpsClock = pg.time.Clock()
        last_move=['0']
        x=get_map(mmap, it)
        man_pos,box_pos,barrier_pos,dest_pos,space_pos=x[0],x[1],x[2],x[3],x[4]
        out=0
        while True:
            screen.fill(black)
            draw_flip(screen,man_pos,box_pos,barrier_pos,dest_pos)
            move(man_pos,box_pos,barrier_pos,space_pos,last_move)
            for event in pg.event.get():
                if event.type==QUIT:
                    pg.quit()
                    sys.exit()
            if game_pass(screen,box_pos,dest_pos)==1:
                while True:
                    screen.fill(black)
                    pg.font.init()
                    fontObj=pg.font.SysFont('SimHei', 18)
                    textSurfaceObj=fontObj.render('关卡通过', True, white,black)
                    textRectObj=textSurfaceObj.get_rect()
                    textRectObj.center=(100,100)
                    screen.blit(textSurfaceObj, textRectObj)
                    if next_task()==1:
                        out=1
                        it+=1
                        break
            pg.display.update()
            #fpsClock.tick(5)
            if out==1:
                break
        if it>=len(mmap):
            screen.fill(black)
            pg.font.init()
            fontObj=pg.font.SysFont('SimHei', 18)
            textSurfaceObj=fontObj.render('恭喜全部通关！', True, white,black)
            textRectObj=textSurfaceObj.get_rect()
            textRectObj.center=(100,100)
            screen.blit(textSurfaceObj, textRectObj)
            pg.display.update()
            break
    while True:
        for event in pg.event.get():
            if event.type==QUIT:
                pg.quit()
                sys.exit()

if __name__=='__main__':
    main(screen,it,mmap,man_pos,barrier_pos,box_pos,dest_pos)

