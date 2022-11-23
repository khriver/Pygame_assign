from settings import *
from player import *
import math
import pygame as pg

class Bullets:
    def __init__(self,game,angle,gage):
        self.game = game
        self.b1_re = B1_RADIUS_EXPLOSION
        self.b1_m = B1_MASS
        self.b1_x ,self.b1_y = PLAYER_POS
        self.angle = angle
        self.gage = gage
        self.b1_state = 'Stop'
    
    def movement(self):
        speed = B1_SPEED * self.game.delta_time * self.gage


        keys = pg.key.get_pressed()
        if keys[pg.K_l]:
            self.b1_state = 'Fire'
        if self.b1_x > HEIGHT and self.b1_x < 0:
            self.b1_state = 'Stop'

        if self.b1_state == 'Fire':
            dx = math.cos(self.angle) * speed
            dy = math.sin(self.angle) * speed
        
        if self.b1_state == 'Stop':
            dx = 0
            dy = 0
            
        
        self.b1_x += dx
        self.b1_y += dy

        
        

        
        
    def draw(self):
        pg.draw.circle(self.game.screen, 'white', (self.b1_x*50, self.b1_y*50),10)

    def update(self):
        self.movement()
        


