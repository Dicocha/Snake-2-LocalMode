import pygame


class Interface:
    WIN_X = 1366
    WIN_Y = 768
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.NOFRAME)
        self.fps = pygame.time.Clock()
        self.bg_img = pygame.image.load('Resources/bg.jpg')
        self.bg_img = pygame.transform.scale(self.bg_img,(self.WIN_X, self.WIN_Y))

        self.click = False

    def music_menu(self):
        pygame.mixer.music.load('Resources/menu.mp3')
        pygame.mixer.music.play(-1)

    def music_game(self):
        pygame.mixer.music.load('Resources/gameplay.mp3')
        pygame.mixer.music.play(-1)