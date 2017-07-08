from element import Element
from size import Size
from pos import Pos
from font import font_surface

import colour
import pygame

class Text(Element):
    def __init__(self, size=Size(70, 30), text='', font_size=11, pos=(0, 0)):
        super(Text, self).__init__(size, pos)
        self.text = text
        self.font_size = font_size
        self.image = font_surface(self.text, self.font_size)
        self.rect = self.image.get_rect() 
        self.rect.move_ip(pos)

    def update(self, event):
        self.dirty = 1
        