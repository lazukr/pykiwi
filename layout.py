from pos import Pos

import pygame
import colour

class Layout(pygame.sprite.DirtySprite):
    def __init__(self, size, pos=Pos(0,0), border=0, background_colour = colour.WHITE):
        super(Layout, self).__init__(self.groups)
        self.background_colour = background_colour
        self.size = size
        self.pos = pos                
        self.image = pygame.Surface(self.size)
        self.image.fill(self.background_colour)
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.pos)
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
