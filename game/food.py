import random
import pygame


class Food:
    def __init__(self):
        self.spawn = False
        self.position = [
            random.randrange(1, (1366//10)) * 10, 
            random.randrange(1, (768//10)) * 10
        ]

    def draw(self, pscreen):
        pygame.draw.rect(pscreen, (255, 0, 0), pygame.Rect(self.position[0], self.position[1], 15, 15))