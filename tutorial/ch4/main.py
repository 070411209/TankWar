import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    #initialize game and create a dispaly object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")
    # set backgroud color
    bg_color = (230,230,230)

    # game loop
    while True:
        # supervise keyboard and mouse item
        gf.check_events()
        ship.update()
        # fill color
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # visualiaze the window
        pygame.display.flip()
run_game()