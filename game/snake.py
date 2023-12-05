import pygame


class Snake:
    def __init__(self):
        self.speed = 20
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50], [70, 50]]

    def movement(self, pdirection):
        if pdirection == "UP":
            self.position[1] -= 10
        elif pdirection == "DOWN":
            self.position[1] += 10
        elif pdirection == "LEFT":
            self.position[0] -= 10
        elif pdirection == "RIGHT":
            self.position[0] += 10

    def draw(self, pscreen):
        for pos in self.body:
            pygame.draw.rect(pscreen, (255, 255, 255), pygame.Rect(pos[0], pos[1], 15, 15))

    def collision(self, pscore):
        from game_over.game_over_controller import GameOverController
        if self.collision_by_screen() or self.collision_by_yourself():
            GameOverController(pscore)

    def collision_by_screen(self) -> bool:
        return self.position[0] < 0 or self.position[0] > 1356 or self.position[1] < 0 or self.position[1] > 758

    def collision_by_yourself(self) -> bool:
        return self.position in self.body[1:]
