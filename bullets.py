from settings import *
from player import *
import math
import pygame as pg

class Bullets(pg.sprite.Sprite):
    def __init__(self,game,pos):
        super().__init__()
        self.game = game
        # self.angle = angle
        # self.gage = gage
        self.state = 'Ready'
        self.init_pos = pos
        self.__x ,self.__y = self.init_pos


        self.type1_img = pg.image.load('./resources/img/Type1.png')#.convert_alpha()
        self.type1_img = pg.transform.scale(self.type1_img,(50,50))
        self.type1_img = pg.transform.rotate(self.type1_img,135)

        #self.type2_img = pg.image.load('./resources/img/Type2.png')#.convert_alpha

        #self.type1_mask = pg.mask.from_surface(self.type1_img)
        self.rect = self.type1_img.get_rect()
        self.rect.centerx , self.rect.centery = self.__x, self.__y
        #self.type2_mask = pg.mask.from_surface(self.type2_img)
        
        self.radius_expl = B1_RADIUS_EXPLOSION
        self.mass = B1_MASS
        self.bullet_speeed = B1_SPEED
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
            gravity =  self.mass * delta_time
            dx = math.cos(self.angle) * speed
            dy = math.sin(self.angle) * speed - gravity            
            self.__x += dx
            self.__y += dy
        
        if self.__x > WIDTH or self.__x < 0 or self.__y > HEIGHT:
            self.state = 'Stop'

        if self.state == 'Stop' or self.state == 'Ready':
            self.__x, self.__y = self.init_pos

        self.rect.x = self.__x
        self.rect.y = self.__y


    def draw(self):
        if self.state =='Fire':
            #print(self.rect)
            self.game.screen.blit(self.type1_img,(self.__x ,self.__y ))
            #pg.draw.circle(self.game.screen, 'black', (self.__x , self.__y ),10)
        


    def update(self):
        self.weapon_change()
        self.movement()
        

