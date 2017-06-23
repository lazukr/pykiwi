from layout import Layout

import pygame
import colour

class ListLayout(Layout):
    def __init__(self, size):
        super(ListLayout, self).__init__(size)

    def render(self, surface):
        x, y = self.pos
        w, h = self.size
        rect = (x, y, w, h)
        pygame.draw.rect(surface, colour.RED, rect)

        self._render_children(surface)
