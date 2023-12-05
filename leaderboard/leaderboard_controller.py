import pygame
from utils.components.button import Button
from utils.components.interface import Interface
from utils.components.text import Text
from utils.file.file_manager import FileManager

 
class LeaderboardController(Interface):
	def __init__(self):
		super().__init__()
		self.music_menu()
		self.run()
	
	def display_elements(self):
		Text('The 3 best', 60, (255, 255, 255), self.screen, self.WIN_X / 3.5, 50)

		self.btn_back = Button(pygame.Rect(400, 600, 550, 70), 'Back', 40, (255, 255, 255), 580, 595)
		self.btn_back.draw(self.screen)

		self.border = pygame.Rect(0, 0, self.WIN_X, self.WIN_Y)
		pygame.draw.rect(self.screen, (255, 255, 255), self.border, 2)

		iy = 250
		Dict = FileManager.read()
		for name in Dict:
			score = Dict.get(name)
			Text(f"{name}   {score}", 40, (255, 255, 255), self.screen, 550, iy)
			iy += 90

	def handle_click(self, mx, my):
		if self.btn_back.rect.collidepoint(mx, my):
			Text(self.btn_back.text, 40, (130,130,130), self.screen, self.btn_back.textx, self.btn_back.texty)
			if self.click:
				return self.btn_back.text
		return None

	def run(self):
		from menu.menu_controller import MenuController

		while True:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN: 
					if event.button == 1:
						self.click = True

			self.screen.blit(self.bg_img,(0,0))
			self.display_elements()

			mx, my = pygame.mouse.get_pos()
			option_text = self.handle_click(mx, my)
			if option_text == "Back":
				MenuController()

			self.click = False
			pygame.display.update()