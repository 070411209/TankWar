import pygame
from setting import Settings
import functions as f
from bowl import Bowl
from ball import Ball
from button import Button

def catch_ball():
    pygame.init()

    sets = Settings()

    screen = pygame.display.set_mode((sets.bg_width, sets.bg_height))
    pygame.display.set_caption('GAME: Catch Ball')

    bowl = Bowl(screen=screen, sets=sets)
    ball = Ball(screen=screen, sets=sets)
    star_button = Button(screen=screen, sets=sets, test="Star(P)")

    while True:
        f.check_event(bowl=bowl, sets=sets, ball=ball) # 检测屏幕是否退出

        if sets.gameover == False :
            bowl.move_bowl(sets=sets) # 移动碗
            ball.drop_ball(sets=sets) # 掉落球
            f.update_ball(ball=ball, bowl=bowl, sets=sets)

        # 更新屏幕
        f.update_screen(screen=screen, sets=sets, bowl=bowl, ball=ball, button=star_button)

        pygame.display.flip()

catch_ball()

