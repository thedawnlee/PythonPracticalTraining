<h1>实体类
        
        
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
    
        def __init__(self,image_name,speed=1):
            super().__init__()
    
            self.image = pygame.image.load(image_name)
            self.rect = self.image.get_rect()
            self.speed = speed
    
        def update(self):
            self.rect.y+=self.speed
    class Background(GameSprite):
        def __init__(self,is_alt=False):
            super().__init__('images/background.png')
            if is_alt:
                self.rect.y = -self.rect.height
    
        def update(self):
        super().update()
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y = -self.rect.height


    class Enemy(GameSprite):
        def __init__(self):
            super().__init__('images/en.png')
            self.speed=random.randint(1, 5)
            self.rect.bottom = 0
            max_x = SCREEN_RECT.width - self.rect.width
            self.rect.x = random.randint(0,max_x)
        def update(self):
            super().update()
            if self.rect.y>=SCREEN_RECT.height:
                print("飞出去了")
                self.kill()
    class Hero(GameSprite):
        def __init__(self):
            super().__init__("images/hero33_1.png",20)

        #设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-50
        self.bullets = pygame.sprite.Group()
        # self.hero.bullets.update()
        # self.hero.draw(self.screen)
    def update(self):
        self.rect.x+=self.speed
        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.right>SCREEN_RECT.right:
            self.rect.right=SCREEN_RECT.right
    def fire(self):
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
        bullet = Bullet()

        # 2. 设置精灵的位置
        bullet.rect.bottom = self.rect.y - 20
        bullet.rect.centerx = self.rect.centerx

        # 3. 将精灵添加到精灵组
        self.bullets.add(bullet)


    class Bullet(GameSprite):
        def __init__(self):
            super().__init__('images/bullet1.png',-2)
        def update(self):
            super().update()
            if self.rect.bottom<0:
                self.kill()


<h1>main 函数实现类
    
    
        # -*- coding: utf-8 -*-
    # @Time    : 2019/6/21 14:45
    # @Author  : Dawn Lee
    # @Email   : lisantao_tao@outlook.com
    # @File    : main.py
    # @Software: PyCharm
    
    
    
    import pygame
    
    import py_sprite
    HERO_FIRE_EVENT = pygame.USEREVENT+1
        #pygame.time.set_timer(HERO_FIRE_EVENT,500)
        FRAME_PER_SEC=60
        SCREEN_RECT = pygame.Rect(0,0,480,700)
        CREATE_ENEMY_EVENT = pygame.USEREVENT
        #pygame.time.set_timer(CREATE_ENEMY_EVENT,1)
        #pygame.font.SysFont('宋体',16,True)
        class PlaneGanme():
            def __init__(self):
                print("游戏init..")
                self.screen = pygame.display.set_mode(SCREEN_RECT.size)
                self.clock = pygame.time.Clock()
                self.__create_sprites()
                pygame.time.set_timer(HERO_FIRE_EVENT, 5)
                pygame.time.set_timer(CREATE_ENEMY_EVENT, 900000)
            def start_game(self):
                print("游戏开始")
                while True:
                    pygame.init()
                    self.clock.tick(FRAME_PER_SEC)
                    self.__event_hander()
                    self.__check_collide()
                    self.__update_sprite()
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type ==pygame.QUIT:
                            self.__game_over()
                        elif event.type == CREATE_ENEMY_EVENT:
                            print("dijichuchangle")

                elif event.type ==HERO_FIRE_EVENT:
                    self.hero.fire()


    def __create_sprites(self):
        bg1 = py_sprite.Background()
        bg2 = py_sprite.Background(True)
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = py_sprite.Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        # self.bullets = pygame.sprite.Group()
        # self.hero.bullets.update()
        # self.hero.bullets.draw(self.screen)


    def __event_hander(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            if event.type== CREATE_ENEMY_EVENT:
                enemy = py_sprite.Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

    def __check_collide(self):
        pass
    def __update_sprite(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0


    def __game_over(self):
        print("gameOver")
        pygame.quit()
        exit()
    def __check_collide(self):
        # pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        # enemies = pygame.sprite.groupcollide(self.hero,self.enemy_group,True)
        # if len(enemies)>0:
        #     self.hero.kill()
        #     self.__game_over()
        # 1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 2. 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表时候有内容
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            self.__game_over()

    if __name__ == '__main__':
    
        game = PlaneGanme()
        game.start_game()