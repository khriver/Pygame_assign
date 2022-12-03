import pygame as pg
from settings import *

class Wall(pg.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.image = pg.image.load('./resources/img/wall.jpg')
        self.image = pg.transform.scale(self.image,(50,200))
        self.rect = self.image.get_rect()
        self.rect.centerx , self.rect.centery = WIDTH/2, HEIGHT-150
    
    def draw(self):
        self.game.screen.blit(self.image,(WIDTH/2-25,HEIGHT-250))