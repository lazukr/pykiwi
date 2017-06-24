from layout import Layout
from pos import Pos
from size import Size

import pygame
import colour

class ListLayout(Layout):
    def __init__(self, size, pos=Pos(0,0), border=5, orientation="vertical", spacing=2):
        super(ListLayout, self).__init__(size, pos, border)
        self.next_child_origin = Pos(
            self.origin.x + self.pos.x + self.border, 
            self.origin.y + self.pos.y + self.border
        )
        self.orientation = orientation
        self.spacing = spacing

    def add(self, child):

        if not self.children:
            self.size = Size(
                child.size.w + 2*self.border,
                child.size.h + 2*self.border
            )
        else:
            if self.orientation == "horizontal":
                self.size = Size(
                self.size.w + child.size.w + self.spacing, 
                self.size.h
            )
            else:
                self.size = Size(
                self.size.w, 
                self.size.h + child.size.h + self.spacing
            )

        self.children.append(child)
        child.origin = self.next_child_origin

        if self.orientation == "horizontal":
            self.next_child_origin = Pos(
                self.next_child_origin.x + child.size.w + self.spacing,
                self.next_child_origin.y
            )

        else:
            self.next_child_origin = Pos(
                self.next_child_origin.x,
                self.next_child_origin.y + child.size.h + self.spacing
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
