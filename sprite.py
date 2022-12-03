from settings import *
from bullets import *
import pygame as pg
import math



class Sprite(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.hp = SPRITE_HP
        self.game = game
        self.x, self.y = SPRITE_POS
        self.img_ready = pg.image.load('./resources/img/sprite_ready.png')
        self.img_ready = pg.transform.scale(self.img_ready,(120,213))
        
        self.img_hit = pg.image.load('./resources/img/sprite_hit.png')
        self.img_hit = pg.transform.scale(self.img_hit,(120,213))

        self.bomb_img = pg.image.load('./resources/img/rocket.png')
        self.bomb_img = pg.transform.scale(self.bomb_img,(100,100))
        


        self.rect = self.img_ready.get_rect()
        self.rect.centerx , self.rect.centery = self.x, self.y+20
        self.turns = False
        self.hitted = False
        self.time_delay = False
        
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


    def hit_delay(self):
        if self.time_delay:
            pg.time.delay(1000)
            self.game.bullets_player.state = 'Stop'
            self.hitted = False
            self.time_delay = False
        else :
            pass


        
        
    def draw(self):
        
        self.hit_delay()    
        if self.hitted:
            self.game.screen.blit(self.img_hit,(self.x-60,self.y-107))
            self.game.screen.blit(self.bomb_img,(self.game.bullets_player.x-100,self.game.bullets_player.y-100))
            self.hp -= 0.1
            self.time_delay = True
            
            
        else:
            self.game.screen.blit(self.img_ready,(self.x-60 ,self.y-107))

        if self.turns == True:
            if self.game.bullets_sprite.state == 'Ready':
                pg.draw.line(self.game.screen, 'yellow',(self.x  , self.y), (self.x + 250 * math.cos(self.angle), self.y + 250 * math.sin(self.angle)), 4)
                pg.draw.line(self.game.screen, 'blue',(self.x   - 30, self.y   +70),(self.x   - 30, self.y   +70 - self.gage*70 - 7), 7)
 
                
    def update(self):


        if self.turns :
            self.movement()
        

