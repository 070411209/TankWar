import pygame
import random
 
 
# 子弹
class Bullet(object):
    # 初始化子弹
    def __init__(self, scene, enemy=False):
        # 子弹移动速度
        self.speed = 1
        # 是否是敌人子弹
        self.is_enemy = enemy
        # 子弹资源
        if self.is_enemy:
            # 加载敌人子弹图片
            self.image = pygame.image.load("./res/bullet_1.png")
            # 设置子弹移动方向
            self.speed = self.speed
        else:
            # 加载英雄子弹图片
            self.image = pygame.image.load("./res/bullet_11.png")
            # 设置子弹移动方向
            self.speed = -self.speed
        # 子弹是否可见
        self.visible = False
        # 持有主场景对象
        self.main_scene = scene
        # 获得子弹矩形(x, y, width, height)
        self.rect = self.image.get_rect()
 
    # 设置子弹位置
    def set_pos(self, x, y):
        self.rect[0] = x
        self.rect[1] = y
 
    # 设置子弹速度
    def set_speed(self, speed):
        if self.is_enemy:
            self.speed = speed
        else:
            self.speed = -speed
 
    # 子弹移动
    def action(self):
        if not self.visible:
            return
        # 假设飞机矩形为plane_rect(10, 20, 200, 300)
        # plane_rect.move_ip(10, 20), 那么结果是plane_rect(20, 40, 200, 300)
        # 也就是原矩形x和y坐标加上move_ip函数x和y坐标，就是当前矩形新位置
        self.rect.move_ip(0, self.speed)
        # 如果子弹超出场景范围,则设置为不可见
        if self.rect[1] < 0 or self.rect[1] > self.main_scene.size[1]:
            self.visible = False
 
    # 绘制子弹
    def draw(self):
        if not self.visible:
            return
        self.main_scene.scene.blit(self.image, (self.rect[0], self.rect[1]))
 
 
# 地图
class GameBackground(object):
    # 初始化地图
    def __init__(self, scene):
        # 加载相同张图片资源,做交替实现地图滚动
        self.image1 = pygame.image.load("res/img_bg_level_3.jpg")
        self.image2 = pygame.image.load("res/img_bg_level_3.jpg")
        # 保存场景对象
        self.main_scene = scene
        # 辅助移动地图
        self.y1 = 0
        self.y2 = -self.main_scene.size[1]
 
    # 计算地图图片绘制坐标
    def action(self):
        self.y1 = self.y1 + 1
        self.y2 = self.y2 + 1
        if self.y1 >= self.main_scene.size[1]:
            self.y1 = 0
        if self.y2 >= 0:
            self.y2 = -self.main_scene.size[1]
 
    # 绘制地图的两张图片
    def draw(self):
        self.main_scene.scene.blit(self.image1, (0, self.y1))
        self.main_scene.scene.blit(self.image2, (0, self.y2))
 
# 飞机
class HeroPlane(object):
    # 飞机初始化
    def __init__(self, scene):
        # 加载飞机资源
        self.image = pygame.image.load("./res/hero2.png")
        # 缓存主场景对象
        self.main_scene = scene
        # 飞机矩形
        self.rect = self.image.get_rect()
        # 矩形起始点
        self.rect[0] = self.main_scene.size[0] / 2 - self.rect[2] / 2
        self.rect[1] = self.main_scene.size[1] - self.rect[3] * 2
        # 飞机子弹列表
        self.bullets = [Bullet(self.main_scene) for _ in range(1, 30)]
 
    # 获得飞机  self.mImage = pygame.image.load("./res/bullet_11.png")矩形
    def rect(self):
        return self.rect
 
    # 发子弹
    def shot(self):
        # 每次发射三颗子弹
        wait_for_shot = []
        # 从子弹列表取出3颗目前尚未发射的子弹
        # 如果子弹的visible为false，说明子弹尚未发射
        for bullet in self.bullets:
            # 如果子弹不可见,说明子弹闲置状态
            if not bullet.visible:
                wait_for_shot.append(bullet)
                if len(wait_for_shot) >= 3:
                    break
        # 子弹发射位置，从posx位置开始 向右排列三颗子弹
        posx = self.rect[0] - 15
        # 依次设置选择子弹的初始位置，并将其设置为发射状态、移动速度
        for bullet in wait_for_shot:
            bullet.visible = True
            posx = posx + 30
            bullet.set_speed(4)
            bullet.set_pos(posx + 5, self.rect[1] - self.rect[3] / 2)
 
    # 飞机动作
    def action(self, x, y):
        self.rect[0] = x - self.rect[2] / 2
        self.rect[1] = y - self.rect[3] / 2
 
    # 飞机绘制
    def draw(self):
        self.main_scene.scene.blit(
            self.image, (self.rect[0], self.rect[1]))
 
# 敌人飞机
class EnemyPlane(object):
    # 初始化敌人飞机
    def __init__(self, scene):
        # 加载飞机资源
        self.image = pygame.image.load("./res/img-plane_1.png")
        # 缓存主场景对象
        self.main_scene = scene
        # 飞机矩形
        self.rect = self.image.get_rect()
        # 子弹列表
        self.bullet = Bullet(self.main_scene, True)
        # 飞机速度
        self.speed = 1
 
    # 获得飞机矩形
    def rect(self):
        return self.rect
 
 
    # 设置飞机位置
    def set_pos(self, x, y):
        self.rect[0] = x
        self.rect[1] = y
 
    # 飞机动作
    def action(self):
        # 子弹每次移动向上移动self.speed速度
        self.rect.move_ip(0, self.speed)
        # 如果飞机移动出屏幕则将飞机设置为不可见状态
        if self.rect[1] > self.main_scene.size[1]:
            # 当飞机飞出屏幕，重新设置飞机的初始位置，移动速度
            # 随机产生x坐标，纵坐标使用为0
            self.set_pos(random.randint(0, self.main_scene.size[1] - self.rect[2] - 20), 0)
            # 随机设置飞机移动速度
            self.speed = random.randint(1, 2)
 
    # 绘制飞机
    def draw(self):
        self.main_scene.scene.blit(self.image, (self.rect[0], self.rect[1]))
 
 
# 主场景
class MainScene(object):
    # 初始化主场景
    def __init__(self):
        # 场景尺寸
        self.size = (512, 768)
        # 场景对象
        self.scene = pygame.display.set_mode([self.size[0], self.size[1]])
        # 设置标题
        pygame.display.set_caption("飞机大战-v1.0")
        # 地图对象
        self.map = GameBackground(self)
        # 英雄对象
        self.hero = HeroPlane(self)
        # 创建多个敌机
        self.enemy_list = [EnemyPlane(self) for _ in range(3)]
 
 
    # 绘制
    def draw_elements(self):
        # 绘制地图
        self.map.draw()
        # 绘制英雄飞机
        self.hero.draw()
        # 依次绘制英雄飞机每一颗发射出去的子弹
        for bullet in self.hero.bullets:
            if bullet.visible:
                bullet.draw()
        # 绘制敌人飞机和飞机子弹
        for plane in self.enemy_list:
            plane.draw()
 
 
    # 动作
    def action_elements(self):
        # 计算坐标地图
        self.map.action()
        # 依次计算英雄飞机每一颗发射子弹的坐标
        for bullet in self.hero.bullets:
            if bullet.visible:
                bullet.action()
        # 计算敌人飞机和其飞机子弹
        for plane in self.enemy_list:
            plane.action()
 
    # 处理事件
    def handle_event(self):
        # 如果玩家点击右上角的X按钮，则关闭窗口
        event_list = pygame.event.get()
        # 遍历事件列表
        for event in event_list:
            # 如果判断用户点击了X按钮，则结束程序
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # 判断事件类型是否是键盘按下事件
            if event.type == pygame.KEYDOWN:
                # 如果是键盘按下，再判断玩家按下的是不是j键
                if event.key == pygame.K_j:
                    self.hero.shot()
 
            # 判断是否发生了鼠标拖动事件
            if event.type == pygame.MOUSEMOTION:
                # 获得鼠标点击三个按钮的点击情况(1,0,0)
                # 如果第一个参数为1,表示左键被按下
                # 如果第二个参数为1,表示滚轮被按下
                # 如果第三个参数为1,表示右键被按下
                buttons = pygame.mouse.get_pressed()
                # 我们只处理左键被按下的情况
                if buttons[0]:
                    # 获得拖动鼠标的拖动位置
                    position = pygame.mouse.get_pos()
                    # 飞机跟随坐标移动
                    # print(position)
                    self.hero.action(position[0], position[1])
 
 
 
    # 碰撞检测
    def detect_conlision(self):
        # 检测英雄子弹是否和敌机碰撞
        for bullet in self.hero.bullets:
            # 如果子弹不可见，说明子弹处于闲置状态，直接continue
            if not bullet.visible:
                continue
            for enemy in self.enemy_list:
                # 判断子弹的矩形和飞机的矩形是否相交
                if pygame.Rect.colliderect(bullet.rect, enemy.rect):
                    # 子弹设置为不可见
                    bullet.visible = False
                    # 敌人飞机重新设置位置和速度
                    enemy.set_pos(random.randint(0, self.size[1] - enemy.rect[2] - 20), 0)
                    enemy.speed = random.randint(1, 2)
                    break
 
    # 主循环,主要处理各种事件
    def run_scene(self):
 
        while True:
            # 计算元素坐标
            self.action_elements()
            # 绘制元素图片
            self.draw_elements()
            # 处理事件
            self.handle_event()
            # 碰撞检测
            self.detect_conlision()
            # 刷新显示
            pygame.display.update()
 
 
# 入口函数
if __name__ == "__main__":
    # 创建主场景
    mainScene = MainScene()
    # 开始游戏
    mainScene.run_scene()