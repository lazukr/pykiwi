from element import Element
from size import Size
from pos import Pos

import pygame
import colour

ANTIALIAS_ON = 1

class Button(Element):
    def __init__(self, text):
        super(Button, self).__init__(Size(70, 30))
        self.text = text

    def render(self, surface):
        abs_pos = Pos(self.origin.x + self.pos.x, self.origin.y + self.pos.y)
        rect = (
            abs_pos.x,
            abs_pos.y, 
            self.size.w, 
            self.size.h
        )
        pygame.draw.rect(surface, colour.GREEN, rect)
        # TODO move font initialization somewhere else
        font = pygame.font.SysFont("monospace", 11)
        label = font.render(self.text, ANTIALIAS_ON, colour.BLACK)
        surface.blit(label, (abs_pos.x, abs_pos.y))


