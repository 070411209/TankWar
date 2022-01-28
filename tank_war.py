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

    @staticmethod
    def __init_game():
        """
        初始化游戏的一些设置
        :return:
        """
        pygame.init()   # 初始化pygame模块
        pygame.display.set_caption(Settings.GAME_NAME)  # 设置窗口标题
        pygame.mixer.init()    # 初始化音频模块

    def __create_mapping(self):
        self.hero = Hero(Settings.HERO_IMAGE_NAME, self.screen, 1)
        self.man = Hero(Settings.MAN_IMAGE_NAME, self.screen, 0)
        self.walls = pygame.sprite.Group()
        self.__draw_map()

    def __create_sprite(self):
        self.hero = Hero(Settings.HERO_IMAGE_NAME, self.screen, 1)
        self.man = Hero(Settings.MAN_IMAGE_NAME, self.screen, 0)
        self.enemies = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for i in range(Settings.ENEMY_COUNT):
            direction = random.randint(0, 3)
            enemy = Enemy(Settings.ENEMY_IMAGES[direction], self.screen)
            enemy.direction = direction
            self.enemies.add(enemy)
        self.__draw_map()

    def __draw_map(self):
        """
        绘制地图
        :return:
        """
        for y in range(len(Settings.MAP_ONE)):
            for x in range(len(Settings.MAP_ONE[y])):
                if Settings.MAP_ONE[y][x] == 0:
                    continue
                wall = Wall(Settings.WALLS[Settings.MAP_ONE[y][x]], self.screen)
                wall.rect.x = x*Settings.BOX_SIZE
                wall.rect.y = y*Settings.BOX_SIZE
                if Settings.MAP_ONE[y][x] == Settings.RED_WALL:
                    wall.type = Settings.RED_WALL
                elif Settings.MAP_ONE[y][x] == Settings.IRON_WALL:
                    wall.type = Settings.IRON_WALL
                elif Settings.MAP_ONE[y][x] == Settings.WEED_WALL:
                    wall.type = Settings.WEED_WALL
                elif Settings.MAP_ONE[y][x] == Settings.BOSS_WALL:
                    wall.type = Settings.BOSS_WALL
                    wall.life = 1
                self.walls.add(wall)

    def __check_keydown(self, event):
        """检查按下按钮的事件"""
        if event.key == pygame.K_j:
            # 按下左键
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_l:
            # 按下右键
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_i:
            # 按下上键
            self.hero.direction = Settings.UP
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_k:
            # 按下下键
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_SPACE:
            # 坦克发子弹
            self.hero.shot()
        # Man
        elif event.key == pygame.K_a:
            # 按下左键
            self.man.direction = Settings.LEFT
            self.man.is_moving = True
            self.man.is_hit_wall = False
        elif event.key == pygame.K_d:
            # 按下右键
            self.man.direction = Settings.RIGHT
            self.man.is_moving = True
            self.man.is_hit_wall = False
        elif event.key == pygame.K_w:
            # 按下上键
            self.man.direction = Settings.UP
            self.man.is_moving = True
            self.man.is_hit_wall = False
        elif event.key == pygame.K_s:
            # 按下下键
            self.man.direction = Settings.DOWN
            self.man.is_moving = True
            self.man.is_hit_wall = False
        elif event.key == pygame.K_r:
            # 坦克发子弹
            self.man.shot()

    def __check_keyup(self, event):
        """检查松开按钮的事件"""
        if event.key == pygame.K_j:
            # 松开左键
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = False
        elif event.key == pygame.K_l:
            # 松开右键
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = False
        elif event.key == pygame.K_i:
            # 松开上键
            self.hero.direction = Settings.UP
            self.hero.is_moving = False
        elif event.key == pygame.K_k:
            # 松开下键
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = False
        # MAN
        elif event.key == pygame.K_a:
            # 松开左键
            self.man.direction = Settings.LEFT
            self.man.is_moving = False
        elif event.key == pygame.K_d:
            # 松开右键
            self.man.direction = Settings.RIGHT
            self.man.is_moving = False
        elif event.key == pygame.K_w:
            # 松开上键
            self.man.direction = Settings.UP
            self.man.is_moving = False
        elif event.key == pygame.K_s:
            # 松开下键
            self.man.direction = Settings.DOWN
            self.man.is_moving = False

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否是退出游戏
            if event.type == pygame.QUIT:
                TankWar.__game_over()
            elif event.type == pygame.KEYDOWN:
                TankWar.__check_keydown(self, event)
            elif event.type == pygame.KEYUP:
                TankWar.__check_keyup(self, event)

    def __check_obstacle(self):
        self.hero.hit_wall()
        self.man.hit_wall()
        # 中墙
        for wall in self.walls:
            # 我方英雄子弹击中墙
            for bullet in self.hero.bullets:
                if pygame.sprite.collide_rect(wall, bullet):
                    if wall.type == Settings.RED_WALL:
                        wall.kill()
                        bullet.kill()
                    elif wall.type == Settings.BOSS_WALL:
                        self.game_still = False
                    elif wall.type == Settings.IRON_WALL:
                        bullet.kill()  
            # 我方英雄子弹击中墙
            for bullet in self.man.bullets:
                if pygame.sprite.collide_rect(wall, bullet):
                    if wall.type == Settings.RED_WALL:
                        wall.kill()
                        bullet.kill()
                    elif wall.type == Settings.BOSS_WALL:
                        self.game_still = False
                    elif wall.type == Settings.IRON_WALL:
                        bullet.kill()                                   
            # 我方坦克撞墙
            if pygame.sprite.collide_rect(self.hero, wall):
                # 不可穿越墙
                if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                    self.hero.is_hit_wall = True
                    # 移出墙内
                    self.hero.move_out_wall(wall)    
            # 我方坦克撞墙
            if pygame.sprite.collide_rect(self.man, wall):
                # 不可穿越墙
                if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                    self.man.is_hit_wall = True
                    # 移出墙内
                    self.man.move_out_wall(wall) 
        # 子弹击中、敌方坦克碰撞、敌我坦克碰撞
        # pygame.sprite.groupcollide(self.hero.bullets, self.man.bullets, True, True)
        # 敌方子弹击中我方
        for bullet in self.man.bullets:
            if pygame.sprite.collide_rect(bullet, self.hero) and self.hero.is_alive:
                bullet.kill()
                self.hero.kill()
                print("--->>> bullet to hero")

        for bullet in self.hero.bullets:
            if pygame.sprite.collide_rect(bullet, self.man) and self.man.is_alive:
                bullet.kill()
                self.man.kill()
                print("--->>> bullet to mans")

    def __check_collide(self):
        # 保证坦克不移出屏幕
        self.hero.hit_wall()
        for enemy in self.enemies:
            enemy.hit_wall_turn()

        # 子弹击中墙
        for wall in self.walls:
            # 我方英雄子弹击中墙
            for bullet in self.hero.bullets:
                if pygame.sprite.collide_rect(wall, bullet):
                    if wall.type == Settings.RED_WALL:
                        wall.kill()
                        bullet.kill()
                    elif wall.type == Settings.BOSS_WALL:
                        self.game_still = False
                    elif wall.type == Settings.IRON_WALL:
                        bullet.kill()
            # 敌方英雄子弹击中墙
            for enemy in self.enemies:
                for bullet in enemy.bullets:
                    if pygame.sprite.collide_rect(wall, bullet):
                        if wall.type == Settings.RED_WALL:
                            wall.kill()
                            bullet.kill()
                        elif wall.type == Settings.BOSS_WALL:
                            self.game_still = False
                        elif wall.type == Settings.IRON_WALL:
                            bullet.kill()

            # 我方坦克撞墙
            if pygame.sprite.collide_rect(self.hero, wall):
                # 不可穿越墙
                if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                    self.hero.is_hit_wall = True
                    # 移出墙内
                    self.hero.move_out_wall(wall)

            # 敌方坦克撞墙
            for enemy in self.enemies:
                if pygame.sprite.collide_rect(wall, enemy):
                    if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                        enemy.move_out_wall(wall)
                        enemy.random_turn()

        # 子弹击中、敌方坦克碰撞、敌我坦克碰撞
        pygame.sprite.groupcollide(self.hero.bullets, self.enemies, True, True)
        # 敌方子弹击中我方
        for enemy in self.enemies:
            for bullet in enemy.bullets:
                if pygame.sprite.collide_rect(bullet, self.hero):
                    bullet.kill()
                    self.hero.kill()

    def __update_sprites(self):
        if self.hero.is_moving and self.hero.alive:
            self.hero.update()
        self.walls.update()
        self.hero.bullets.update()
        self.enemies.update()
        for enemy in self.enemies:
            enemy.bullets.update()
            enemy.bullets.draw(self.screen)
        self.enemies.draw(self.screen)
        self.hero.bullets.draw(self.screen)
        self.screen.blit(self.hero.image, self.hero.rect)
        self.walls.draw(self.screen)

    def __update_walls(self):
        if self.hero.is_moving and self.hero.is_alive:
            self.hero.update()
        if self.hero.is_alive:
            self.hero.bullets.update()
            self.hero.bullets.draw(self.screen)
            self.screen.blit(self.hero.image, self.hero.rect)

        if self.man.is_moving and self.man.is_alive:
            self.man.update()
        if self.man.is_alive:
            self.man.bullets.update()
            self.man.bullets.draw(self.screen)
            self.screen.blit(self.man.image, self.man.rect)
        
        
        self.walls.update()
        self.walls.draw(self.screen)

    def run_game(self):
        self.__init_game()
        self.__create_sprite()
        while True and self.hero.is_alive and self.game_still:
            self.screen.fill(Settings.SCREEN_COLOR)
            # 1、设置刷新帧率
            self.clock.tick(Settings.FPS)
            # 2、事件监听
            self.__event_handler()
            # 3、碰撞监测
            self.__check_collide()
            # 4、更新/绘制精灵/经理组
            self.__update_sprites()
            # 5、更新显示
            pygame.display.update()
        self.__game_over()

    def play_game(self):
        self.__init_game()
        self.__create_mapping()
        while True and self.game_still:
            self.screen.fill(Settings.SCREEN_COLOR)
            self.clock.tick(Settings.FPS)
            self.__event_handler()
            self.__check_obstacle()
            self.__update_walls()
            pygame.display.update()
        self.__game_over()

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()



