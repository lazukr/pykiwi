from layout import Layout
from pos import Pos

import pygame
import colour

class ListLayout(Layout):
    def __init__(self, size, pos=Pos(0,0)):
        super(ListLayout, self).__init__(size, pos)
        self.next_child_origin = Pos(
            self.origin.x + self.pos.x, 
            self.origin.y + self.pos.y
        )

    def add(self, child):
        self.children.append(child)
        child.origin = self.next_child_origin
        self.next_child_origin = Pos(
            self.next_child_origin.x,
            self.next_child_origin.y + child.size.h
        )

    def render(self, surface):
        rect = (
            self.origin.x + self.pos.x,
            self.origin.y + self.pos.y, 
            self.size.w, 
            self.size.h
        )
        pygame.draw.rect(surface, colour.RED, rect)

        self._render_children(surface)
