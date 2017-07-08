from element import Element
from size import Size
from pos import Pos
from font import font_surface
from text import Text

import colour
import pygame

class Button(Element):
    def __init__(self, text, font_size=11, size=Size(70, 30), pos=Pos(0, 0), background_colour=colour.WHITE):
        super(Button, self).__init__(size, pos, background_colour)
        self.text = text
        self.font_size = font_size
        self.image = pygame.Surface(size)
        self.image.fill(self.background_colour)
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)
        self.callbacks_dict = {
            '1': self._null_event,
            '2': self._null_event,
            '3': self._null_event,
            '4': self._mouse_hover,
            '5': self._mouse_down,
            '6': self._mouse_up
        }
        self.text_image = Text(size=self.size, text=self.text, pos=self.pos)

    def update(self, event):
        self.callbacks_dict[str(event.type)]()
        
    def _null_event(self):
        pass

    def _mouse_down(self):
        if self.will_collide():
            self.mouse_down_event()
            self.mouse_click_event()
            self.dirty = 1

    def _mouse_hover(self):
        if self.will_collide():
            self.mouse_hover_in_event()
            self.dirty = 1
        else:
            self.mouse_hover_out_event()
            self.dirty = 1

    def _mouse_up(self):
        self.mouse_up_event()
        self.dirty = 1

    def mouse_click_event(self):
        print 'hi'

    def mouse_down_event(self):
        self.image.fill(colour.GREEN)

    def mouse_up_event(self):
        self.image.fill(self.background_colour)

    def mouse_hover_in_event(self):
        self.image.set_alpha(200)

    def mouse_hover_out_event(self):
        self.image.set_alpha(255)

    def move(self, delta):
        self.rect.move_ip(delta)
        self.text_image.rect.move_ip(delta)

