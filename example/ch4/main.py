from pickle import NONE
import pygame
from sprites import *


class TankWar:

    def __init__(self):
        self.screen = pygame.display.set_mode(Settings.SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.game_still = True
        self.hero = None
        self.enemies = None
        self.enemy_bullets = None
        self.walls = None
        self.textImage = None
        self.is_change = False
        self.x = 100
        self.y = 100
        self.buffer_text = ''
        self.word = 'START'
        self.char_ = ''
        self.c = (255,0,0)
        self.ret = 0
        self.is_put = True
        self.start_time = None
        self.init_ = pygame.init()
        self.myfont = pygame.font.Font(None, 100)

    def __create_sprite(self):
        self.hero = Hero(Settings.HERO_IMAGE_NAME, self.screen)

    def __update_sprites(self):
        if self.hero.is_moving and self.hero.alive:
            self.hero.update()
        self.screen.blit(self.hero.image, self.hero.rect)

    def __update_text(self):
        if self.is_put:
            # 记录数据
            self.word = self.word + self.char_
            self.buffer_text = self.buffer_text + self.char_
            
        if self.is_change:
            print("----- RESULT >>>>>> ", self.ret)
            print("----- INPUT >>>>>> ", self.buffer_text)
            self.x, self.y, self.word, self.c, self.ret = TankWar.get_random_word(self)
            self.buffer_text = ''

        self.textImage = self.myfont.render(self.word, True, self.c)
        self.screen.blit(self.textImage, (self.x, self.y))

    def __check_collide(self):
        # 保证坦克不移出屏幕
        self.hero.hit_wall()

    def get_random_word(self):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # 颜色随机
        x = random.randint(100, 500)  # x坐标从左右边距各100之间随机
        y = random.randint(100, 500)
        a = random.randint(2, 9)
        b = random.randint(1, 10)
        ret = a + b
        word = str(a)+str('+')+str(b)+str('=')
        return x, y, word, color, ret

    @staticmethod
    def __init_game():
        """
        初始化游戏的一些设置
        :return:
        """
        pygame.init()   # 初始化pygame模块
        pygame.display.set_caption(Settings.GAME_NAME)  # 设置窗口标题
        pygame.mixer.init()    # 初始化音频模块

    def __check_keydown(self, event):
        """检查按下按钮的事件"""
        if event.key == pygame.K_LEFT:
            # 按下左键
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_RIGHT:
            # 按下右键
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_UP:
            # 按下上键
            self.hero.direction = Settings.UP
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_DOWN:
            # 按下下键
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_SPACE:
            # 坦克发子弹
            self.is_change = True
        else :
            self.is_put = True  
            self.char_ = chr(event.key)          

    def __check_keyup(self, event):
        """检查松开按钮的事件"""
        if event.key == pygame.K_LEFT:
            # 松开左键
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = False
        elif event.key == pygame.K_RIGHT:
            # 松开右键
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = False
        elif event.key == pygame.K_UP:
            # 松开上键
            self.hero.direction = Settings.UP
            self.hero.is_moving = False
        elif event.key == pygame.K_DOWN:
            # 松开下键
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = False
        elif event.key == pygame.K_SPACE:
            self.is_change = False
        else:
            self.is_put = False


    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否是退出游戏
            if event.type == pygame.QUIT:
                TankWar.__game_over()
            elif event.type == pygame.KEYDOWN:
                TankWar.__check_keydown(self, event)
            elif event.type == pygame.KEYUP:
                TankWar.__check_keyup(self, event)

    def update_time(self):
        end_time = pygame.time.get_ticks()  
        time = (end_time - self.start_time)//1000
        text_surface = self.myfont.render("System Time:" + str(time), True, "blue")
        self.screen.blit(text_surface, (0,0))

    def run_game(self):
        self.__init_game()
        self.__create_sprite()
        self.start_time = pygame.time.get_ticks()
        while True and self.game_still:
            self.screen.fill(Settings.SCREEN_COLOR)
            # 1、设置刷新帧率
            self.clock.tick(Settings.FPS)
            # 2、事件监听
            self.__event_handler()
            pygame.time.wait(100)
            # 3、碰撞监测
            self.__check_collide()            
            # 4、更新/绘制精灵/经理组
            self.__update_sprites()
            # 5、更新文字
            self.__update_text()    
            # 更新时间
            self.update_time()
            # 5、更新显示
            pygame.display.update()              
            
        self.__game_over()

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()



if __name__ == '__main__':
    tankWar = TankWar()
    tankWar.run_game()

