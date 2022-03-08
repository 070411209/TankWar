
# encoding: utf-8

import pygame
import sys
import random
import socket
from threading import Thread
import time

import redis

def save():
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    r.set('foo', 'my_redis')
    print( r.get('foo'))
    r.delete('foo')
    r.save()

def server_run():
    clients = []
    my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_server.bind(("", 1024))
    my_server.listen(256)
    my_server.setblocking(False)   


def SendToServer(is_save = 0):
    package = socket.recv(1000)

def my_counter():
    i = 0
    for x in range(10000):
        i = i + 1
    return True
def run():
    thread_array = {}
    start_time = time.time()
    for tt in range(2):
        t = Thread(target=my_counter)
        t.start()
        thread_array[time.tid] = t
    for i in range(2):
        thread_array[i].join()
    end_time = time.time()
    print("count time: {}".format(end_time - start_time))


class go_sock(object):
    ip = ""
    port = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self):
        object.__init__(self)
    def connect(self, ip, port): 
        self.ip = ip
        self.port = port
        self.sock.connect_ex((ip, port))
    def close(self):
        self.sock.close()

    def used(self):
        _inet = go_sock()
        _inet.connect("115.231.74.62", 21)
        _inet.sock.recv(100)

class explode(pygame.sprite.Sprite):
    def __init__(self, target, frame, single_w, single_h, pos=(0, 0)):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(target).convert_alpha()

        self.main_image = self.image

        self.frame = frame

        self.rect = self.image.get_rect()

        self.count = 0

        self.single_w, self.single_h = single_w, single_h

        self.rect.topleft = pos


    def update(self):

        if self.count < self.frame-1:

            self.count += 1

        else:

            self.count = 0

        self.image = self.main_image.subsurface([self.count*self.single_w, 0, self.single_w,self.single_h])


class Geek:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.plane = 'bg.png'
        self.text = "tt"
        self.txt = u"暂停" 

        self.fnt = pygame.font.SysFont('微软雅黑',32)

    def blit_squences(self, data, x, y):
        if isinstance(data, list):
            for d in data:
                self.screen.blit(d, (x, y))
        else:
            self.screen.blit(data, (x, y))

    def pygame_test(self):
        background = 'wall.png'
        
        total = 10
        wall = []
        right_1 = 'right_1.png'
        right_2 = 'right_2.png'

        player = 'human.png'
        plr = pygame.image.load(player).convert_alpha()
        init_x = 0
        init_y = 300
        step_x = 62
        step_y = -30

        r_1 = pygame.image.load(right_1).convert_alpha()
        r_2 = pygame.image.load(right_2).convert_alpha()
        y_move = 0

        # 初始化
        pygame.init()
        pygame.mixer.init()
        # 创建一个窗口
        self.screen = pygame.display.set_mode((800, 600))
        # 设置窗口标题
        pygame.display.set_caption('这是一个窗口标题')

        pln = pygame.image.load(self.plane).convert_alpha()
        self.screen.blit(pln, (40, 350))
        pygame.display.update()

        bg = pygame.image.load(background).convert()


        pygame.mixer.music.load('bgm.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        s1 = pygame.mixer.Sound('a.wav') 
        s1.set_volume(0.5)
        s2 = pygame.mixer.Sound('b.wav')
        s2.set_volume(0.5)

        # 行为

        pln_t = pygame.transform.flip(pln, 1, 1)
        self.screen.blit(pln_t, (40, 350))

        pln_t = pygame.transform.scale(pln, (220, 220))
        self.screen.blit(pln_t, (20, 150))

        pln_t = pygame.transform.rotate(pln, 20)

        pln_t = pygame.transform.chop(pln, [20, 150, 25, 155])
        self.screen.blit(pln_t, (20, 150))
        enemy = 'enemy.png'
        enm = pygame.image.load(enemy).convert_alpha()

        pygame.mouse.get_pressed()[0]

        ex1 = random.randrange(20, 600)
        ey1 = random.randrange(10, 50)
        ex2 = random.randrange(20, 600)
        ey2 = random.randrange(10, 50)
        ex3 = random.randrange(20, 600)
        ey3 = random.randrange(10, 50)

        fnt = pygame.font.Font('freesansbold.ttf',25)
        the_rect = pygame.Rect(200, 100, 150, 40)
        block_surface = self.screen.subsurface(the_rect).copy()
        # pygame.Font.render(pygame.text, pygame.antialias, pygame.color, background=None)
        tsurf = fnt.render(self.text, True, (255,255,255))
        trect = tsurf.get_rect()
        trect.center = ((block_surface.get_width()/2),(block_surface.get_height()/2))
        
        mouse = 'mouse.png'
        mouse_cursor = pygame.image.load(mouse).convert_alpha()
        mouse_scale = pygame.transform.scale(mouse_cursor, (40, 40))

        xx = 0
        yy = 0
        txt = "Pause"
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] :
            if x >=200 and x <= 350 and y >= 200 and y <= 240:
                txt = "Clicked"

        while total > 0:
            if total % 2 == 0:
                wall.append(r_1)
            else:
                wall.append(r_2)
            total -= 1

        # 通过不断循环来侦听事件
        while True:
            # get():获取事件的返回值
            for event in pygame.event.get():
                # 判断事件是否是退出事件，是则退出
                if event.type == pygame.QUIT:
                    # 先退出pygame窗口，再退出程序
                    pygame.quit()
                    sys.exit()

            self.screen.blit(bg, (0, y_move))

            for w in wall:
                self.screen.blit(w, (init_x, init_y))
                init_x += step_x
                init_y += step_y

            for w in wall:
                if init_y == 270:
                    self.blit_squences([plr, w], init_x, init_y)
                else:
                    self.blit_squences(w, init_x, init_y)
                init_x += step_x
                init_y += step_y

            exp = explode('explode.png', 3, 262,262, (100,100))
            group = pygame.sprite.Group()
            group.add(exp)

            group.update()
            group.draw(self.screen)    


            self.screen.blit(enm, (ex1, ey1))
            self.screen.blit(enm, (ex2, ey2))
            self.screen.blit(enm, (ex3, ey3))
            ey1 +=1
            ey2 +=1
            ey3 +=1

            y1, y2 = 1, 1
            self.screen.blit(pln, (100, 300 + y1))
            self.screen.blit(enm, (100, 20 + y2))
            print(self.collide(pln, (100,300+y1), enm, (100,20+y2)))
            y1-=1
            y2+=1 


            if True == self.collide(pln, (100,300+y1), enm, (100,20+y2)):
                s1.play()
            else:
                s2.play()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            pygame.mixer.music.pause()
                        if event.key == pygame.K_r:
                            pygame.mixer.music.unpause()                         



            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                yy -= 1
            if key[pygame.K_s]:
                yy += 1
            if key[pygame.K_a]:
                xx -= 1
            if key[pygame.K_d]:
                xx += 1

            if key[pygame.K_w] and key[pygame.K_LCTRL]:
                yy -= 2 
            print( key)

 
            #获取 x, y 值
            x-= mouse_scale.get_width() / 2
            y-= mouse_scale.get_height() / 2
            self.screen.blit(mouse_scale, (x, y))        

            self.screen.blit(block_surface, (200, 200))
            block_surface.fill([0,20,0])
            self.text_out(txt)

            self.screen.blit(plr, (62, 270))
            pygame.display.update()

    def play_test1(self):

        pln = pygame.image.load(self.plane).convert()
        a=0
        while True: 
            pln.set_alpha(a)
            self.screen.blit(pln, (20, 150))
            if a > 255:
                a=0
            self.screen.fill([a,a,a])
            a += 1    


    def collide(self, a, axy,  b, bxy):
        a_x1, a_x2 = axy[0], axy[0]+a.get_width()
        a_y1, a_y2 = axy[1], axy[1]+a.get_height()
        b_x1, b_x2 = bxy[0], bxy[0]+b.get_width()
        b_y1, b_y2 = bxy[1], bxy[1]+b.get_height()
        a1, a2 = range(a_x1, a_x2) , range(a_y1, a_y2)
        b1, b2 = range(b_x1, b_x2) , range(b_y1, b_y2) 

        ct = 0
        for a in a1:
            if a in b1:
                ct = 1
                break
        for a in a2:
            if a in b2:
                if ct == 1:
                    return True
        return False


    def text_out(self, text):
        the_rect = pygame.Rect(200, 100, 150, 40)
        block_surface = self.screen.subsurface(the_rect).copy()        
        fnt = pygame.font.Font('freesansbold.ttf',25)
        tsurf = fnt.render(text, True, (255,255,255))
        trect = tsurf.get_rect()
        trect.center = ((block_surface.get_width()/2),(block_surface.get_height()/2))
        block_surface.blit(tsurf, trect)
        
if __name__ == '__main__':
    geek = Geek()
    geek.pygame_test()

