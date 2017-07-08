import pygame
import colour

from pos import Pos

class Element(pygame.sprite.DirtySprite):

    def __init__(self, size, pos=Pos(0, 0), background_colour=colour.WHITE):
        super(Element, self).__init__(self.groups)

        self.background_colour = background_colour
        self.size = size
        self.pos = pos
        self.image = pygame.Surface(size)
        self.image.fill(self.background_colour)
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)

    def will_collide(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self):
        raise NotImplementedError

    def mouse_down_event(self):
        raise NotImplementedError

    def mouse_up_event(self):
        raise NotImplementedError

    def mouse_hover_in_event(self):
        raise NotImplementedError

    def mouse_hover_out_event(self):
        raise NotImplementedError

    def _mouse_down(self):
        raise NotImplementedError

    def _mouse_up(self):
        raise NotImplementedError

    def _mouse_hover(self):
        raise NotImplementedError




