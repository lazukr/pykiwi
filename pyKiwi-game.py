from core import Core
from listlayout import ListLayout
from button import Button
from size import Size
from pos import Pos
from text import Text

import styles
import orientation
import colour
import events
import pygame

SCREEN_SIZE = (640, 480)
FPS = 30

def button_click():
    print 'poke'

def okay_duh():
    print 'okay_duh'


class Game(object):
    def __init__(self):
        self.fps = FPS
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.background = pygame.Surface(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.core = Core()


        

    def initialize(self):
        pygame.display.init()
        pygame.font.init()
        pygame.display.flip()

        #button = Button('click me', pos=Pos(50, 50))
        # anotherbutton = Button('click me')
        layout = ListLayout(border=2, spacing=3, pos=Pos(30, 50))
        for x in range(5):
            button = Button('click me')
            layout.add_element(button)

        
        # # all user custom code should go here
        # # and ui stuff


    def start(self):
        running = True

        while running:
            self.clock.tick(self.fps)
            pygame.display.set_caption('{0}'.format(self.clock.get_fps()))
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    running = False

                self.core.all_ui.update(event)
         
            self.core.all_ui.clear(self.screen, self.background)
            
            dirty = self.core.all_ui.draw(self.screen)
            pygame.display.update(dirty)       
            

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.initialize()
    game.start()
