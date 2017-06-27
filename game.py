from collections import defaultdict
from listener import Listener
from pos import Pos

import pygame
import events
import hover
import colour

SCREEN_SIZE = (640, 480)

class Game(object):
    def __init__(self, dim=SCREEN_SIZE, fps=30, background_color=(255,255,255)):
        self.dim = dim
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.background_color = background_color
        self.screen = None

        self.listeners = defaultdict(list)

    def on(self, element, evt, callback=None):
        listener = Listener(element, callback)
        self.listeners[evt].append(listener)

    def on_mouse_down(self):
        mouse_pos = pygame.mouse.get_pos()
        click_listeners = self.listeners[events.CLICK]
        for listener in click_listeners:
            if listener.element.will_collide(mouse_pos):
                listener.callback()

    def on_mouse_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        hover_listeners = self.listeners[events.HOVER]

        for listener in hover_listeners:

            if listener.element.hover(mouse_pos) == hover.HOVER_DEACTIVATED:
                listener.element.hover_state = hover.NO_HOVER
                self.view.remove(listener.element.hover_element)

            elif listener.element.hover(mouse_pos) == hover.ON_HOVER_ACTIVATED:
                listener.element.hover_state = hover.HOVER_ACTIVATED
                listener.element.hover_element.origin = Pos(mouse_pos[0], mouse_pos[1] + 10)
                self.view.append(listener.element.hover_element)
                
    def start(self):
        pygame.display.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode(self.dim)
        is_running = True

        self.render_root()

        while is_running:
            self.clock.tick(self.fps)

            self.screen.fill(colour.BLACK)
            for view in self.view:
                view.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_mouse_down()
                
                self.render()
            self.on_mouse_hover()

            pygame.display.flip()
        pygame.quit()

    def render(self):
        raise NotImplementedError

    def render_root(self):
        raise NotImplementedError
