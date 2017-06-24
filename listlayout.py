from layout import Layout
from pos import Pos
from size import Size

import pygame
import colour, styles, orientation

class ListLayout(Layout):
    def __init__(self, size, pos=Pos(0,0), border=0, spacing=0,
        orientation=orientation.VERTICAL, scaling=styles.FREE):
        
        super(ListLayout, self).__init__(size, pos, border)
        self.next_child_origin = Pos(
            self.origin.x + self.pos.x + self.border, 
            self.origin.y + self.pos.y + self.border
        )
        self.orientation = orientation
        self.spacing = spacing
        self.scaling = scaling

    def add(self, child):

        if self.scaling:
            self._rescale_layout(child)

        self.children.append(child)
        child.origin = self.next_child_origin

        self._update_child_pos(child)

    def render(self, surface):
        rect = (
            self.origin.x + self.pos.x,
            self.origin.y + self.pos.y, 
            self.size.w, 
            self.size.h
        )
        pygame.draw.rect(surface, colour.RED, rect)

        self._render_children(surface)

    def _rescale_layout(self, child):
        if not self.children:
            self.size = Size(
                child.size.w + 2*self.border,
                child.size.h + 2*self.border
            )
        else:
            self.size = Size(
            self.size.w + (child.size.w + self.spacing)*int(self.orientation), 
            self.size.h + (child.size.h + self.spacing)*int(not self.orientation)
            )

    def _update_child_pos(self, child):
        self.next_child_origin = Pos(
            self.next_child_origin.x + (child.size.w + self.spacing)*int(self.orientation),
            self.next_child_origin.y + (child.size.h + self.spacing)*int(not self.orientation)
        )
