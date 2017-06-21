# this implements ui elements
import pygame


class UIElement:

    def __init__(self, dim=(1, 1), pos=(0, 0), background_color=(255, 255, 255)):
        self.dim = dim
        self.background_color = background_color
        self.element = pygame.Rect((0, 0), self.dim)
        self.element.move_ip(pos)

    def SetBackgroundColour(self, color):
        self.background_color = color

    def SetWidth(self, width):
        self.width = width

    def SetHeight(self, height):
        self.height = height

    def SetDimensions(self, width, height):
        self.width = width
        self.height = height

    def update(self, screen):
        pygame.draw.rect(screen, self.background_color, self.element)

