import sys
import pygame
from utils.components.button import Button
from utils.components.input import Input
from utils.components.interface import Interface
from utils.components.text import Text
from utils.file.file_manager import FileManager


class GameOverController(Interface):
	def __init__(self, pscore):
		super().__init__()

		self.score = pscore
		self.name = ''
		self.message = ''
		self.menu_buttons = [
			Button(pygame.Rect(520, 400, 300, 70), 'Retry', 35, (255, 255, 255), 590, 400),
			Button(pygame.Rect(520, 500, 300, 70), 'Save', 35, (255, 255, 255), 600, 500),
			Button(pygame.Rect(520, 600, 300, 70), 'Exit', 35, (255, 255, 255), 600, 600)
		]

		self.run()
 
	def display_elements(self):
		Text(f"Your score: {self.score}", 50, (255, 255, 255), self.screen, self.WIN_X/3.6, 40)
		Text('Nombre: ', 30, (255, 255, 255), self.screen, 460, 250)
		Text(self.message, 10, (255, 255, 255), self.screen, self.WIN_X-120, self.WIN_Y-25)

		self.input = Input(pygame.Rect(710, 250, 200, 70), self.name, 30, (255, 255, 255))
		self.input.draw(self.screen)

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
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						self.name = self.name[:-1]
					
					else: 
						self.name += event.unicode

						if self.input.limit():
							self.name = self.name[:-1]

				elif event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						self.click = True

			self.screen.blit(self.bg_img,(0,0))
			self.display_elements()
			self.input.update_text(self.name)

			mx, my = pygame.mouse.get_pos()
			option_text = self.handle_click(mx, my)

			if option_text == "Retry":
				GameController()

			elif option_text == "Save":
				FileManager.insert(self.name.capitalize, self.score)
				self.message = 'Guardado!!'

			elif option_text == "Exit":
				pygame.quit()
				sys.exit()

			self.click = False
			pygame.display.update()
			pygame.display.flip()