import pygame as pg
from settings import *

class UI:
    
    def __init__(self,game):
        self.game = game
        self.hp_l = PLAYER_HP
        self.hp_r = SPRITE_HP
        

    def update(self,hp1,hp2):
        self.hp_l = hp1
        self.hp_r = hp2



    def draw(self):
        
        pg.draw.line(self.game.screen, 'red',(80,60),(80+self.hp_l*400,60),35)
        pg.draw.line(self.game.screen, 'red',(WIDTH-80,60),(WIDTH-80-self.hp_r*400,60),35)
        pg.draw.rect(self.game.screen, 'black',(80,40,404,39),5)
        pg.draw.rect(self.game.screen, 'black',(WIDTH-80-400,40,404,39),5)


