import pygame


class Input:
    def __init__(self, rect, text, size, color):
        self.rect = rect
        self.text = text
        self.size = size
        self.color = color
        self.font = pygame.font.Font("Resources/Jackpot.ttf", self.size)
        self.render_text()

    def limit(self):
        return self.text_surface.get_width() > self.rect.w - 120

    def render_text(self):
        self.text_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.text_surface, (self.rect.x + 40, self.rect.y + 5))

    def update_text(self, new_text):
        self.text = new_text
        self.render_text()