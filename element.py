import pygame
import colour

class Element(object):
    def __init__(self, size, pos=(0, 0), background_color=colour.WHITE):
        self.size = size
        self.pos = pos
        self.background_color = background_color

    def render(self, surface):
        raise NotImplementedError
