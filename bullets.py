from settings import *
from player import *
import math
import pygame as pg

class Bullets:
    def __init__(self,game,angle,gage):
        self.game = game
        self.radius_expl = B1_RADIUS_EXPLOSION
        self.mass = B1_MASS
        self.bullet_speeed = B1_SPEED
        self.x ,self.y = PLAYER_POS
        self.angle = angle
        self.gage = gage
        self.state = 'Ready'
        self.type = '1'

    
    def weapon_change(self):

        if pg.key.get_pressed()[pg.K_1]:
            self.radius_expl = B1_RADIUS_EXPLOSION
            self.mass = B1_MASS
            self.bullet_speeed = B1_SPEED
            self.type = '1'
        
        if pg.key.get_pressed()[pg.K_2]:
            self.radius_expl = B2_RADIUS_EXPLOSION
            self.mass = B2_MASS
            self.bullet_speeed = B2_SPEED
            self.type = '2'
        
    
    def update_pos(self, angle, gage):
        self.angle = angle
        self.gage = gage

    
    def movement(self):
        speed = self.bullet_speeed * self.game.delta_time * self.gage
        dx = 0
        dy = 0


        if pg.key.get_pressed()[pg.K_l]:
            if self.state == 'Fire': pass #중복 방지
            else :
                self.state = 'Fire'
                self.fire_time = pg.time.get_ticks()

        if self.state == 'Fire':
            delta_time = self.fire_time - pg.time.get_ticks()
            gravity =  self.mass * delta_time * 0.00003
            dx = math.cos(self.angle) * speed
            dy = math.sin(self.angle) * speed - gravity            
            self.x += dx
            self.y += dy
        
        if self.x * 50 > WIDTH or self.x * 50 < 0 or self.y * 50 > HEIGHT:
            self.state = 'Stop'

        if self.state == 'Stop' or self.state == 'Ready':
            self.x, self.y = PLAYER_POS
            

    def draw(self):
        if self.state =='Fire':
            pg.draw.circle(self.game.screen, 'white', (self.x*50, self.y*50),10)
        


    def update(self):
        self.weapon_change()
        self.movement()
        


