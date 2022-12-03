from settings import *
import pygame as pg
import random

class Weather:
    def __init__(self,game):
        self.game = game
        self.image = pg.image.load('./resources/img/weather.png')
        self.image = pg.transform.scale(self.image,(80,64))
        self.wind = (random.random()-0.5)/2000
        self.windforshow = abs(round(self.wind*20000,3))

    def update(self):
        self.wind = (random.random()-0.5)/2000
        self.windforshow = abs(round(self.wind*20000,3))
        if self.wind >= 0:
            self.image = pg.image.load('./resources/img/weather.png')
            self.image = pg.transform.scale(self.image,(80,64))
        else :
            self.image = pg.transform.rotate(pg.image.load('./resources/img/weather.png'),180)
            self.image = pg.transform.scale(self.image,(80,64))
        print(self.wind)

    def draw(self):
        font = pg.font.SysFont(None,35)
        font_surf = font.render(f'wind : {self.windforshow} m/s',True,'black')
        self.game.screen.blit(self.image,(WIDTH/2-40,28))
        self.game.screen.blit(font_surf, (WIDTH/2-font_surf.get_rect().width/2,100))

