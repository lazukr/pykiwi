from element import Element

import pygame
import colour

class Button(Element):
    def __init__(self, label):
        super(Button, self).__init__((10,10))
        self.label = label

    def render(self, surface):
        x, y = self.pos
        w, h = self.size
        rect = (x, y, w, h)
        pygame.draw.rect(surface, colour.GREEN, rect)
