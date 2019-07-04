# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 15:17
# @Author  : Dawn Lee
# @Email   : lisantao_tao@outlook.com
# @File    : py_sprite.py
# @Software: PyCharm
import pygame
import random


SCREEN_RECT = pygame.Rect(0, 0, 480, 700)


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__('images/background.png')
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        super().__init__('images/enemy0.png')
        self.speed = random.randint(1, 5)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出去了")
            self.kill()
class EnemyX(GameSprite):
    def __init__(self):
        super().__init__('images/enemy1.png')
        self.speed = random.randint(1, 5)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出去了")
            self.kill()


class Hero(GameSprite):
    def __init__(self,imgsrc="images/cxk_1.png",speedX=0):
        super().__init__(imgsrc,20)
        self.speedx = speedX
        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 50
        self.bullets = pygame.sprite.Group()
        # self.hero.bullets.update()
        # self.hero.draw(self.screen)


    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        self.rect.y +=self.speedx
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self,imgsrc,speed=-2):
        print("发射子弹")
        # 1. 创建子弹精灵
        # for i in range(20):
        #     bullet = Bullet()
        #
        #     # 2. 设置精灵的位置
        #     bullet.rect.bottom = self.rect.y - 20
        #     bullet.rect.centerx = self.rect.centerx
        #
        #     # 3. 将精灵添加到精灵组
        #     self.bullets.add(bullet)
        bullet = Bullet(imgsrc,speed)

        # 2. 设置精灵的位置
        bullet.rect.bottom = self.rect.y - 20
        bullet.rect.centerx = self.rect.centerx

        # 3. 将精灵添加到精灵组
        self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self,imgsrc,speed):
        super().__init__(imgsrc, speed)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

class IKUN(GameSprite):
    def __init__(self):
        super().__init__('images/cxk_.png')
        self.speed = random.randint(1, 5)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出去了")
            self.kill()
