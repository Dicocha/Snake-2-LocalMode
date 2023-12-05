import pygame
from utils.components.text import Text


class Button:
    def __init__(self, prect, ptext, psize, pcolor, ptextx, ptexty):
        self.rect = prect
        self.text = ptext
        self.font = psize
        self.color = pcolor
        self.textx = ptextx
        self.texty = ptexty

    def draw(self, pscreen):
        pygame.draw.rect(pscreen, self.color, self.rect, 2)
        Text(self.text, self.font, self.color, pscreen, self.textx, self.texty)