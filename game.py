import pygame as pg
import sys
from map import *
from settings import *
from player import *
from sprite import *
from bullets import *

class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode(WindowSize)
		self.clock = pg.time.Clock()
		self.delta_time = 1
		self.new_game()
	
	def new_game(self):
		self.map = Map(self)
		self.player = Player(self)
		self.sprite = Sprite(self)

	def update(self):
		self.player.update()
		self.sprite.update()
		pg.display.flip()
		self.delta_time = self.clock.tick(FPS)

	def draw(self):
		self.screen.fill('white')
		self.map.draw()
		self.player.draw()
		self.sprite.draw(self.screen)
	
	def check_events(self):
		if self.player.turns == True and self.player.bullets.state == 'Stop':
			self.sprite.turns = True
			self.sprite.bullets.state = 'Ready'
			self.player.turns = False
		if self.sprite.turns == True and self.sprite.bullets.state == 'Stop':
			self.player.turns = True
			self.player.bullets.state ='Ready'
			self.sprite.turns = False

		for event in pg.event.get():
			if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
				pg.quit()
				sys.exit()
	
	def run(self):
		while True:
			self.check_events()
			self.update()
			self.draw()

	


if __name__ == '__main__':
	game = Game()
	game.run()