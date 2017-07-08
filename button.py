from element import Element
from size import Size
from pos import Pos
from font import font_surface
from text import Text

import colour
import pygame
import events
import alpha

class Button(Element):
    def __init__(self, text, font_size=11, size=Size(70, 30), pos=Pos(0, 0), background_colour=colour.WHITE):
        super(Button, self).__init__(size, pos, background_colour)
        self.text = text
        self.font_size = font_size

        self.callbacks_dict = {
            events.MOUSEMOTION : self._mouse_hover,
            events.MOUSEBUTTONDOWN : self._mouse_down,
            events.MOUSEBUTTONUP : self._mouse_up
        }
        self.text_image = Text(size=self.size, text=self.text, pos=self.pos)

    def update(self, event):
        if str(event.type) in self.callbacks_dict:
            self.callbacks_dict[str(event.type)]()

    def _mouse_down(self):
        if self.will_collide():
            self.on_mouse_down_event()
            self.on_mouse_click_event()
            self.dirty = 1

    def _mouse_hover(self):
        if self.will_collide():
            self.on_mouse_hover_in_event()
            self.dirty = 1
        else:
            self.on_mouse_hover_out_event()
            self.dirty = 1

    def _mouse_up(self):
        self.on_mouse_up_event()
        self.dirty = 1

    def on_mouse_click_event(self):
        print 'hi'

    def on_mouse_down_event(self):
        self.image.fill(colour.GREEN)

    def on_mouse_up_event(self):
        self.image.fill(self.background_colour)

    def on_mouse_hover_in_event(self):
        self.image.set_alpha(alpha.TRANSPARENT)

    def on_mouse_hover_out_event(self):
        self.image.set_alpha(alpha.OPAQUE)

    def move(self, delta):
        self.rect.move_ip(delta)
        self.text_image.rect.move_ip(delta)

