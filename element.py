import pygame
import colour

from pos import Pos

class Element(object):
    def __init__(self, size, pos=Pos(0, 0), background_color=colour.WHITE):
        self.size = size
        self.pos = pos
        self.origin = Pos(0, 0)
        self.background_color = background_color
        self.container = None

    def will_collide(self, mouse_pos):
        return self.container.collidepoint(mouse_pos)

    def render(self, surface):
        raise NotImplementedError
