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
		self.bullets_player = Bullets(self,PLAYER_POS)
		self.bullets_sprite = Bullets(self,SPRITE_POS)

	def update(self):
		self.player.update()
		self.sprite.update()
		self.bullets_player.update_pos(self.player.angle,self.player.gage)
		self.bullets_player.update()
		self.bullets_sprite.update_pos(self.sprite.angle,self.sprite.gage)
		self.bullets_sprite.update()
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
	
	def check_events(self):
		if self.player.turns == True and self.bullets_player.state == 'Stop':
			self.player.turns = False
			self.sprite.turns = True
			self.bullets_sprite.state = 'Ready'
			
		if self.sprite.turns == True and self.bullets_sprite.state == 'Stop':
			self.sprite.turns = False
			self.player.turns = True
			self.bullets_player.state ='Ready'
			

		for event in pg.event.get():
			if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
				pg.quit()
				sys.exit()
	
	def run(self):
		while True:
			if self.sprite.rect.colliderect(self.bullets_player.rect):
				self.bullets_player.state = 'Stop'
				self.bullets_player.rect
			self.check_events()
			self.update()
			#print(self.bullets_player.get_rect(),self.bullets_sprite.get_rect())
			self.draw()
			#print(self.player.turns,self.bullets_player.state,self.sprite.turns,self.bullets_sprite.state)

	


if __name__ == '__main__':
	game = Game()
	game.run()