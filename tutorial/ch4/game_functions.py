import sys
import pygame




def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        #move right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #move right
        ship.moving_left = True 
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        #move right
        ship.moving_left = False
def check_events(ship):
    #respond to  keyboard and mouse item
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        
def update(self):
    if self.moving_right:
        self.rect.centerx +=1


def update_screen(ai_settings,screen,ship):
    # fill color
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # visualiaze the window
    pygame.display.flip()
    