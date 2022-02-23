import pygame.font

class Button():
    def  __init__(self, screen, sets, test):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.sets = sets
        self.test = test # 文字

        self.width = self.sets.button_width
        self.height = self.sets.button_height
        self.button_bg_color = self.sets.button_bg_color
        self.button_word_color = self.sets.button_word_color
        self.font = pygame.font.SysFont(None, 48)

        # rect对象
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_test(test) # 建立按钮标签，只需要建立一次

    # 建立按钮
    def prep_test(self, test):
        # 将文本转化为图像
        self.test_image = self.font.render(self.test, True, self.button_word_color,self.button_bg_color)
        self.test_image_rect = self.test_image.get_rect()
        self.test_image_rect.center = self.rect.center

    # 绘制按钮
    def draw_button(self):
        self.screen.fill(self.button_bg_color, self.rect)
        self.screen.blit(self.test_image, self.test_image_rect)
