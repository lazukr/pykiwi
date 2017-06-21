import pygame
import colour

class Element:
    def __init__(self, size, pos=(0, 0), background_color=colour.WHITE):
        self.size = size
        self.pos = pos
        self.background_color = background_color

    def update(self, screen):
        pass
