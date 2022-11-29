from settings import *
from bullets import *
import pygame as pg
import math

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.turns = True
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.gage = 0.1
        self.gage_state = 'UP'
        self.bullets = Bullets(self.game, self.angle, self.gage)

    def movement(self):
        speed = PLAYER_SPEED * self.game.delta_time
        rot_speed = PLAYER_ROT_SPEED * self.game.delta_time
        delta_gage , delta_angle = 0,0
        if self.gage > 1:
            self.gage_state = 'DOWN'
        elif self.gage < 0.1:
            self.gage_state = 'UP'

        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            delta_angle -= rot_speed
        if keys[pg.K_DOWN]:
            delta_angle += rot_speed
        
        if keys[pg.K_SPACE]:
            if self.gage_state == 'UP':
                delta_gage += speed
            elif self.gage_state == 'DOWN':
                delta_gage -= speed

        
        self.gage += delta_gage
        self.angle += delta_angle

        if math.degrees(self.angle) < 290:
            self.angle = math.radians(290)
        if math.degrees(self.angle) > 340:
            self.angle = math.radians(340)
        
        self.bullets.update_pos(self.angle, self.gage)
        
        self.bullets.movement()
    
        

        
        
    def draw(self):
        pg.draw.circle(self.game.screen, 'green', (self.x * 50, self.y *50),10)
        if self.turns == True:
            if self.bullets.state == 'Ready':
                pg.draw.line(self.game.screen, 'yellow',(self.x * 50, self.y *50), (self.x*50 + WIDTH * math.cos(self.angle), self.y*50 + HEIGHT * math.sin(self.angle)), 2)
                pg.draw.line(self.game.screen, 'blue',(self.x * 50 + 10, self.y * 50 + 10),(self.x * 50 + 10, self.y * 50 + 10 + self.gage*100 + 10), 2)
            if self.bullets.state=='Fire':
                self.bullets.draw()  
                

    def update(self):
        if self.turns :
            self.movement()

