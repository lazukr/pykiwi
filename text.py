from element import Element
from size import Size
from pos import Pos
from font import font_surface

import colour
import pygame

class Text(Element):
    def __init__(self, size=Size(70, 30), text='', font_size=11):
        super(Text, self).__init__(size)
        self.text = text
        self.font_size = font_size
        self.border = 2

    def render(self, surface):
        abs_pos = Pos(self.origin.x + self.pos.x, self.origin.y + self.pos.y)
        rect = (
            abs_pos.x,
            abs_pos.y, 
            self.size.w, 
            self.size.h
        )
        self.container = pygame.draw.rect(surface, colour.WHITE, rect)
        surface.blit(
            font_surface(self.text, self.font_size),
            (abs_pos.x, abs_pos.y)
        )


