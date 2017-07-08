from layout import Layout
from pos import Pos
from size import Size

import pygame
import colour
import styles
import orientation
import utils

class ListLayout(Layout):
    def __init__(
        self,
        size=Size(50, 50),
        pos=Pos(0,0),
        border=0,
        spacing=0,
        orientation=orientation.VERTICAL,
        scaling=styles.FIT,
        background_colour=colour.RED):
        
        super(ListLayout, self).__init__(size, pos, border, background_colour)
        
        self.image = pygame.Surface(self.size)
        self.image.fill(self.background_colour)
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.pos)

        self.orientation = orientation
        self.spacing = spacing
        self.scaling = scaling
        self.next_child_origin = Pos(
            self.pos.x + self.border,
            self.pos.y + self.border
        )

    def update(self, event):
        pass

    def add_element(self, child):
        if self.scaling:
            self._rescale_layout(child)

        self.children.append(child)
        child.move(self.next_child_origin)

        self._update_child_pos(child)

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

        self.image = pygame.Surface(self.size)
        self.image.fill(self.background_colour)
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.pos)

    def _update_child_pos(self, child):
        self.next_child_origin = Pos(
            self.next_child_origin.x + (child.size.w + self.spacing)*int(self.orientation),
            self.next_child_origin.y + (child.size.h + self.spacing)*int(not self.orientation)
        )