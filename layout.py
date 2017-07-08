from pos import Pos

import pygame
import colour

class Layout(pygame.sprite.DirtySprite):
    def __init__(self, size, pos=Pos(0,0), border=0, background_colour = colour.WHITE):
        pygame.sprite.DirtySprite.__init__(self, self.groups)
        self.background_colour = background_colour
        self.size = size
        self.pos = pos
        self.origin = Pos(0, 0)
        self.children = []
        self.border = border

    def _render_children(self, surface):
        for child in self.children:
            child.draw(surface)

    def add_element(self, child):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError
