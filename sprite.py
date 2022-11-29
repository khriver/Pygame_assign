from settings import *
from bullets import *
import pygame as pg
import math



class Sprite(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.x, self.y = SPRITE_POS
        self.image = pg.image.load('./resources/img/sprite_normal.png')#.convert_alpha
        self.image = pg.transform.scale(self.image,(180,320))
        #self.sprite_mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx , self.rect.centery = self.x, self.y
        self.turns = False
        
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


        
        
    def draw(self, crash = True):
        pg.draw.circle(self.game.screen, 'red', (self.x, self.y),10)
        self.game.screen.blit(self.image,(self.x-90 ,self.y-160))
        if self.turns == True:
            if self.game.bullets_sprite.state == 'Ready':
                pg.draw.line(self.game.screen, 'yellow',(self.x  , self.y), (self.x + WIDTH * math.cos(self.angle), self.y + HEIGHT * math.sin(self.angle)), 2)
                pg.draw.line(self.game.screen, 'blue',(self.x   + 10, self.y   + 10),(self.x   + 10, self.y   + 10 + self.gage*100 + 10), 2)
 
                
    def update(self):

        if self.turns :
            self.movement()
        

