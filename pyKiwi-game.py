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
        self.core = Core(self.screen, self.background)        

    def initialize(self):
        pygame.display.init()
        pygame.font.init()
        pygame.display.flip()

        #button = Button('click me', pos=Pos(50, 50))
        # anotherbutton = Button('click me')

        layout = self.core.create_listlayout(pos=Pos(30, 50), spacing=2, border=3)

        for x in range(5):
            button = self.core.create_button(text='click me')
            layout.add_element(button)


        another_layout = self.core.create_listlayout(background_colour=colour.WHITE)
        for x in range(3):
            another_button = self.core.create_button(text='hi me')
            another_layout.add_element(another_button)

        # layout.add_element(another_layout)
        
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

                self.core.update(event)
         
            self.core.clear()
            
            dirty = self.core.draw()
            pygame.display.update(dirty)
            

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.initialize()
    game.start()
