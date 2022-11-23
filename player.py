from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.gage = 0

    def movement(self):
        speed = PLAYER_SPEED * self.game.delta_time
        rot_speed = PLAYER_ROT_SPEED * self.game.delta_time
        delta_gage , delta_angle = 0,0

        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            delta_angle -= rot_speed
        if keys[pg.K_DOWN]:
            delta_angle += rot_speed
        if keys[pg.K_SPACE]:
            delta_gage += speed

        self.gage += delta_gage
        self.angle += delta_angle

        
        
    def draw(self):
        pg.draw.line(self.game.screen, 'yellow',(self.x * 50, self.y *50), (self.x*50 + WIDTH * math.cos(self.angle), self.y*50 + HEIGHT * math.sin(self.angle)), 2)
        pg.draw.line(self.game.screen, 'yellow',(self.x * 50 + 1, self.y * 50 + 1),(self.x * 50 + 1, self.y * 50 + 1 + self.gage + 1), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 50, self.y *50),10)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def gage_angle(self):
        return self.gage, self.angle
