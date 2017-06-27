import pygame
import colour
import hover

from pos import Pos


class Element(object):
    def __init__(self, size, pos=Pos(0, 0), background_color=colour.WHITE):
        self.size = size
        self.pos = pos
        self.origin = Pos(0, 0)
        self.background_color = background_color
        self.container = None
        self.hover_state = hover.NO_HOVER
        self.hover_activated = False
        self.hover_onset = 20
        self.hover_waited = 0
        self.hover_element = None

    def will_collide(self, mouse_pos):
        return self.container.collidepoint(mouse_pos)

    def hover(self, mouse_pos):

        if not self.hover_element:
            return False

        elif self.container.collidepoint(mouse_pos) and self.hover_state != hover.HOVER_ACTIVATED:
            self.hover_state = hover.ON_HOVER
        
        elif not self.container.collidepoint(mouse_pos) and self.hover_state == hover.HOVER_ACTIVATED:
            self.hover_state = hover.HOVER_DEACTIVATED
            self.hover_waited = 0
            self.hover_activated = False

        if self.hover_state == hover.ON_HOVER:
            self.hover_waited += 1

        if self.hover_waited > self.hover_onset and self.hover_state != hover.HOVER_ACTIVATED:
            self.hover_state = hover.ON_HOVER_ACTIVATED
            self.hover_activated = True

        return self.hover_state

    def attach_hover(self, hover_element):
        self.hover_element = hover_element

    def render(self, surface):
        raise NotImplementedError

    def render_hover(self, surface):
        pass

