import pygame
class Ship():

    def __init__(self,screen):
        #initialize spaceship and its location
        self.screen = screen

        # load bmp image and get rectangle
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put spaceship on the bottom of window
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #buld the spaceship at the specific location
        self.screen.blit(self.image,self.rect)