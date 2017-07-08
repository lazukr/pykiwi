from pos import Pos
from size import Size
from button import Button
from listlayout import ListLayout
from text import Text

import pygame
import events
import colour
import orientation
import styles


class Core(object):
    __instance = None

    def __new__(cls, screen ,background):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, screen, background):
        self.all_ui = pygame.sprite.LayeredDirty()
        Button.groups = self.all_ui
        Text.groups = self.all_ui
        ListLayout.groups = self.all_ui
        self.core_screen = screen
        self.core_background = background
        self.children = []

    def draw(self):
        return self.all_ui.draw(self.core_screen)

    def clear(self):
        self.all_ui.clear(self.core_screen, self.core_background)

    def update(self, event):
        self.all_ui.update(event)

    def create_button(self, *args, **kwargs):
        text = kwargs.get('text', '')
        font_size = kwargs.get('font_size', 11)
        size = kwargs.get('size', Size(70, 30))
        pos = kwargs.get('pos', Pos(0, 0))
        background_colour = kwargs.get('background_colour', colour.WHITE)
        return Button(text, font_size, size, pos, background_colour)

    def create_listlayout(self, *args, **kwargs):
        size = kwargs.get('size', Size(50, 50))
        pos = kwargs.get('pos', Pos(0, 0))
        border = kwargs.get('border', 0)
        spacing = kwargs.get('spacing', 0)
        orient = kwargs.get('orientation', orientation.VERTICAL)
        scale = kwargs.get('scaling', styles.FIT)
        background_colour = kwargs.get('background_colour', colour.RED)
        return ListLayout(size, pos, border, spacing, orient, scale, background_colour)