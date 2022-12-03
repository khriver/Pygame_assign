import pygame as pg
from settings import *

_ = False

map_layout = [
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1]    
]

class Map:
    def __init__(self,game):
        self.game = game
        self.map_layout = map_layout
        self.map = {}
        self.get_map()
        self.russia_flag = pg.image.load('./resources/img/russia.png')
        self.russia_flag = pg.transform.scale(self.russia_flag,(60,40))
        self.ukrine_flag = pg.image.load('./resources/img/ukrine.png')
        self.ukrine_flag = pg.transform.scale(self.ukrine_flag,(60,40))
        self.bg_img = pg.image.load('./resources/img/background.png')
        self.bg_img = pg.transform.scale(self.bg_img,(1200,600))
        self.gr_img = pg.image.load('./resources/img/ground.png')
        self.gr_img = pg.transform.scale(self.gr_img,(50,50))

    
    def get_map(self):
        for j, row in enumerate(self.map_layout):
            for i, value in enumerate(row):
                if value:
                    self.map[(i,j)] = value

    
    def draw(self):
        self.game.screen.blit(self.bg_img,(0,0))
        self.game.screen.blit(self.russia_flag,(WIDTH-70,40))
        self.game.screen.blit(self.ukrine_flag,(10,40))
        [self.game.screen.blit(self.gr_img ,(pos[0]*50, pos[1] * 50))
        for pos in self.map]
        
        # [pg.draw.rect(self.game.screen, 'darkgray', (pos[0]*50, pos[1] * 50, 50, 50))
        # for pos in self.map]
