import pygame
import colour

FONT = 'monospace'
ANTIALIAS_ON = 1

def font_surface(text, size):
    font = pygame.font.SysFont(FONT, size)
    return font.render(text, ANTIALIAS_ON, colour.BLACK)
