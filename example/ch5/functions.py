import sys
import pygame

# 检测屏幕退出
def check_event(bowl, sets, ball):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_LEFT:
                bowl.moving = -1
            if event.key == pygame.K_RIGHT:
                bowl.moving = 1
            if event.key == pygame.K_p: # 按下P开始
                reset_game(sets, ball) # 重置游戏
        elif event.type == pygame.KEYUP:
            bowl.moving = 0

def reset_game(sets, ball):
    sets.gameover = False
    ball.number = 3

# 更新屏幕
def update_screen(screen, sets, bowl, ball, button):
    screen.fill(sets.bg_color)
    bowl.print_bowl()
    ball.print_ball()
    if sets.gameover == True:
        button.draw_button()

# 更新球
def update_ball(ball, bowl, sets):
    if pygame.sprite.collide_rect(ball ,bowl): # 碗接住了球
        ball.change_ball(sets)
        sets.catch_number += 1
        #print(sets.catch_number)
    if check_ball_edge(ball, sets): # 球到底了
        if ball.number > 0:
            ball.number -= 1
            #print(ball.number)
            ball.change_ball(sets)
        else:
            sets.gameover = True

def check_ball_edge(ball, sets):
    if ball.rect.bottom >= sets.bg_height:
        return True
    else:
        return False
