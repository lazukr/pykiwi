from collections import defaultdict
from listener import Listener

import pygame
import events

SCREEN_SIZE = (640, 480)

class Game(object):
    def __init__(self, dim=SCREEN_SIZE, fps=30, background_color=(255,255,255)):
        self.dim = dim
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.background_color = background_color
        self.screen = None

        self.listeners = defaultdict(list)

    def on(self, element, evt, callback):
        listener = Listener(element, callback)
        self.listeners[evt].append(listener)

    def on_mouse_down(self):
        mouse_pos = pygame.mouse.get_pos()
        click_listeners = self.listeners[events.CLICK]
        for listener in click_listeners:
            if listener.element.will_collide(mouse_pos):
                listener.callback()

    def start(self):
        pygame.display.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode(self.dim)
        is_running = True

        root = self.render_root()
        root.render(self.screen)

        while is_running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_mouse_down()
                self.render()

            pygame.display.flip()
        pygame.quit()

    def render(self):
        raise NotImplementedError

    def render_root(self):
        raise NotImplementedError
