from settings import *
from bullets import *
import pygame as pg
import math



class Sprite(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.x, self.y = SPRITE_POS
        self.img_ready = pg.image.load('./resources/img/sprite_ready.png')
        self.img_ready = pg.transform.scale(self.img_ready,(135,240))
        
        self.img_hit = pg.image.load('./resources/img/sprite_hit.png')
        self.img_hit = pg.transform.scale(self.img_hit,(135,240))


        self.rect = self.img_ready.get_rect()
        self.rect.centerx , self.rect.centery = self.x, self.y
        self.turns = False
        self.hitted = False
        
        self.angle = SPRITE_ANGLE
        self.gage = 0.1
        self.gage_state = 'UP'


    def movement(self):
        speed = SPRITE_SPEED * self.game.delta_time
        rot_speed = SPRITE_ROT_SPEED * self.game.delta_time
        delta_gage , delta_angle = 0,0
        
        if self.gage > 1:
            self.gage_state = 'DOWN'
        elif self.gage < 0.1:
            self.gage_state = 'UP'

        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            delta_angle += rot_speed
        if keys[pg.K_DOWN]:
            delta_angle -= rot_speed
        
        if keys[pg.K_SPACE]:
            if self.gage_state == 'UP':
                delta_gage += speed
            elif self.gage_state == 'DOWN':
                delta_gage -= speed

        
        self.gage += delta_gage
        self.angle += delta_angle

        if math.degrees(self.angle) < 200:
            self.angle = math.radians(200)
        if math.degrees(self.angle) > 250:
            self.angle = math.radians(250)


        
        
    def draw(self, crash = True):
        pg.draw.circle(self.game.screen, 'red', (self.x, self.y),10)
        
        if self.hitted:
            self.game.screen.blit(self.img_hit,(self.x-90,self.y-160))
        else:
            self.game.screen.blit(self.img_ready,(self.x-90 ,self.y-160))

        if self.turns == True:
            if self.game.bullets_sprite.state == 'Ready':
                pg.draw.line(self.game.screen, 'yellow',(self.x  , self.y), (self.x + WIDTH * math.cos(self.angle), self.y + HEIGHT * math.sin(self.angle)), 2)
                pg.draw.line(self.game.screen, 'blue',(self.x   + 10, self.y   + 10),(self.x   + 10, self.y   + 10 + self.gage*100 + 10), 2)
 
                
    def update(self):

        if self.turns :
            self.movement()
        

