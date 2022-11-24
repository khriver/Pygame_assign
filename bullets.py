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
    
    def update_pos(self, angle, gage):
        self.angle = angle
        self.gage = gage

    
    def movement(self):
        speed = B1_SPEED * self.game.delta_time * self.gage


        if pg.key.get_pressed()[pg.K_l]:
            if self.b1_state == 'Fire': pass #중복 방지
            else :
                self.b1_state = 'Fire'
                self.fire_time = pg.time.get_ticks()

        if self.b1_state == 'Fire':
            delta_time = self.fire_time - pg.time.get_ticks()
            gravity =  self.b1_m * delta_time * 0.00003
            dx = math.cos(self.angle) * speed
            dy = math.sin(self.angle) * speed - gravity            
            self.b1_x += dx
            self.b1_y += dy
        
        if self.b1_x * 50 > WIDTH or self.b1_x * 50 < 0 or self.b1_y * 50 > HEIGHT:
            self.b1_state = 'Stop'

        if self.b1_state == 'Stop':
            dx = 0
            dy = 0
            self.b1_x ,self.b1_y = PLAYER_POS
            

    def draw(self):
        pg.draw.circle(self.game.screen, 'white', (self.b1_x*50, self.b1_y*50),10)


    def update(self):
        self.movement()
        


