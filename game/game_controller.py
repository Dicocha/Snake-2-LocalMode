import pygame
from game.food import Food
from game.snake import Snake
from utils.components.interface import Interface
from utils.components.text import Text


class GameController(Interface):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.direction = "RIGHT"
		self.change_to = self.direction
		self.food = Food()
		self.music_game()
		self.run()

	def spawn_new_food(self):
		# Create a new instance of the Food class
		self.food = Food()
	
	def display_elements(self):
		self.screen.blit(self.bg_img,(0,0))

		pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(0, 0, self.WIN_X, self.WIN_Y), 2)

		Text(f"Score: {str(self.score)}", 20, (255, 255, 255), self.screen, self.WIN_X/2.4, 2)

		self.snake.draw(self.screen)

		if not self.food.spawn:
			self.food.draw(self.screen)
			self.food.spawn == True
 
	def user_inputs(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					self.change_to = "UP"
				elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
					self.change_to = "DOWN"
				elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
					self.change_to = "LEFT"
				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					self.change_to = "RIGHT"

		if self.change_to == "UP" and self.direction != "DOWN":
			self.direction = "UP"
		elif self.change_to == "DOWN" and self.direction != "UP":
			self.direction = "DOWN"
		elif self.change_to == "LEFT" and self.direction != "RIGHT":
			self.direction = "LEFT"
		elif self.change_to == "RIGHT" and self.direction != "LEFT":
			self.direction = "RIGHT"

		self.snake.movement(self.direction)

	def eat(self) -> bool:
		self.snake.body.insert(0, list(self.snake.position))

		if self.snake.position == self.food.position:
			self.score += 1
			self.snake.speed += 2
			self.spawn_new_food()
			
		else:
			self.snake.body.pop()

	def run(self):
		self.snake = Snake()
		
		while True:
			self.display_elements()
			self.user_inputs()
			self.eat()
			self.snake.collision(self.score)

			pygame.display.update()
			self.fps.tick(self.snake.speed)