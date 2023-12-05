import pygame


class Text:
    def __init__(self, ptext, psize, pcolor, psurface, px, py):
        self.size = psize
        self.font = pygame.font.Font("Resources/Jackpot.ttf", self.size)

        self.textobj = self.font.render(ptext, True, pcolor)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (px, py)
        self.draw(psurface)

    def draw(self, psurface):
        psurface.blit(self.textobj, self.textrect)