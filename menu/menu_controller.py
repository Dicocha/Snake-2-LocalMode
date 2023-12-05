import sys
import pygame
from utils.components.interface import Interface
from utils.components.button import Button
from utils.components.text import Text

class MenuController(Interface):
    def __init__(self):
        super().__init__()
        self.music_menu()

        self.menu_buttons = [
            Button(pygame.Rect(480, 300, 400, 70), 'Start', 40, (255, 255, 255), 576.4, 298),
            Button(pygame.Rect(480, 400, 400, 70), 'Scores', 40, (255, 255, 255), 556.4, 395),
            Button(pygame.Rect(480, 500, 400, 70), 'Exit', 40, (255, 255, 255), 596.4, 495)
        ]
 
        self.run()

    def display_elements(self):
        self.screen.blit(self.bg_img, (0, 0))
        
        Text('SNAKE 2', 60, (255, 255, 255), self.screen, self.WIN_X/2.8, 80)

        self.border = pygame.Rect(0, 0, self.WIN_X, self.WIN_Y)
        pygame.draw.rect(self.screen, (255, 255, 255), self.border, 2)

        for entity in self.menu_buttons:
            entity.draw(self.screen)

    def handle_click(self, mx, my):
        for entity in self.menu_buttons:
            if entity.rect.collidepoint(mx, my):
                Text(entity.text, entity.font, (130,130,130), self.screen, entity.textx, entity.texty)
                if self.click:
                    return entity.text
        return None
    
    def run(self):
        from game.game_controller import GameController
        from leaderboard.leaderboard_controller import LeaderboardController

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            self.display_elements()

            mx, my = pygame.mouse.get_pos()
            option_text = self.handle_click(mx,my)
            if option_text == "Start":
                GameController()

            elif option_text == "Scores":
                LeaderboardController()

            elif option_text == "Exit":
                pygame.quit()
                sys.exit()

            self.click = False

            pygame.display.update()
            self.fps.tick(60)
