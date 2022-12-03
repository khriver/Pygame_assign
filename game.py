import pygame as pg
import sys
from map import *
from settings import *
from player import *
from sprite import *
from bullets import *
from check_events import *
from ui import *
from wall import *
from weather import *

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
		self.bullets_player = Bullets(self,PLAYER_POS,135)
		self.bullets_sprite = Bullets(self,SPRITE_POS,315)
		self.check_event = Checkevents(self)
		self.ui = UI(self)
		self.wall = Wall(self)
		self.weather = Weather(self)

	def update(self):
		self.player.update()
		self.sprite.update()
		self.bullets_player.update_pos(self.player.angle,self.player.gage)
		self.bullets_player.update()
		self.bullets_sprite.update_pos(self.sprite.angle,self.sprite.gage)
		self.bullets_sprite.update()
		self.ui.update(self.player.hp,self.sprite.hp)
		pg.display.flip()
		self.delta_time = self.clock.tick(FPS)

	def draw(self):
		self.screen.fill('white')
		self.map.draw()
		self.player.draw()
		self.sprite.draw()
		if self.bullets_player.state=='Fire' and self.player.turns == True:
			self.bullets_player.draw()  	
		if self.bullets_sprite.state=='Fire' and self.sprite.turns == True:
			self.bullets_sprite.draw()
		self.ui.draw() 
		self.wall.draw()
		self.weather.draw()
	
	def check_events(self):
		self.check_event.turn()
		self.check_event.hit()


		for event in pg.event.get():
			if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
				pg.quit()
				sys.exit()
	
	def run(self):
		while True:

			
			
			self.update()
			self.check_events()
			
			self.draw()
			
			

	


if __name__ == '__main__':
	game = Game()
	game.run()