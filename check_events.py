import pygame as pg
from player import *
from sprite import *
from bullets import *

class Checkevents:
    def __init__(self,game):
        self.game = game
    
    def turn(self):
        if self.game.player.turns == True and self.game.bullets_player.state == 'Stop':
            self.game.player.turns = False
            self.game.sprite.turns = True
            self.game.bullets_sprite.state = 'Ready'
			
        if self.game.sprite.turns == True and self.game.bullets_sprite.state == 'Stop':
            self.game.sprite.turns = False
            self.game.player.turns = True
            self.game.bullets_player.state ='Ready'
    

    def turn(self):
        if self.game.player.turns == True and self.game.bullets_player.state == 'Stop':
            self.game.player.turns = False
            self.game.sprite.turns = True
            self.game.bullets_sprite.state = 'Ready'
			
        if self.game.sprite.turns == True and self.game.bullets_sprite.state == 'Stop':
            self.game.sprite.turns = False
            self.game.player.turns = True
            self.game.bullets_player.state ='Ready'
