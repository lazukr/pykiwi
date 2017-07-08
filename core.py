from collections import defaultdict
from listener import Listener
from pos import Pos
from button import Button
from listlayout import ListLayout
from text import Text

import pygame
import events
import tooltip
import colour


class Core(object):
    def __init__(self):
        self.all_ui = pygame.sprite.LayeredDirty()
        Button.groups = self.all_ui
        Text.groups = self.all_ui
        ListLayout.groups = self.all_ui


    def add_element(self, element):
        self.elements.append(element)
        print 'element added'
        print self.elements


    def del_element(self, element):
        self.elements.remove(element)

    def draw(self, surf=None):
        if surf == None:
            surf = pygame.display.get_surface()

        for element in self.elements:
            element.draw(surf)


