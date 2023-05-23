import pygame
import random
from time import *
pygame.init()


#variables
wid = 800
hig = 600
phat = __file__[0:len(__file__)-8]


#color
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (26, 36, 54)
GREEN = (0, 255, 0)
ORANGE = (247,178, 17)
RED = (255,0,0)
LIGHT_GREY = (120, 120, 120)

#screen
screen = pygame.display.set_mode((wid,hig))
pygame.display.set_caption("FALL DOWN")


#load img
platform = pygame.image.load(f"{phat}/img/platform.png")
platform_r = platform.get_rect(); platform_r.y = 0; platform_r.x = 0

boom1 = pygame.image.load(f"{phat}/img/boom1.png")
boom1_r = boom1.get_rect(); boom1_r.y = 0; boom1_r.x = 0

boom2 = pygame.image.load(f"{phat}/img/boom2.png")
boom2_r = boom2.get_rect(); boom2_r.y = 0; boom2_r.x = 0

boom3 = pygame.image.load(f"{phat}/img/boom3.png")
boom3_r = boom3.get_rect(); boom3_r.y = 0; boom3_r.x = 0

mine = pygame.image.load(f"{phat}/img/mine.png")
mine_r = mine.get_rect(); mine_r.y = 0; mine_r.x = 0

border = pygame.image.load(f"{phat}/img/border.png").convert()
border_r = border.get_rect(); border_r.y = 0; border_r.x = 0

background = pygame.image.load(f"{phat}/img/background.png").convert()
background_r = background.get_rect(); background_r.y = 0; background_r.x = 0

finish = pygame.image.load(f"{phat}/img/finish.png").convert()
finish_r = finish.get_rect(); finish_r.y = 0; finish_r.x = 0

p0 = pygame.image.load(f"{phat}/img/p0.png").convert()
player_r = p0.get_rect(); player_r.y = 0; player_r.x = 0

p1 = pygame.image.load(f"{phat}/img/p1.png").convert()

p2 = pygame.image.load(f"{phat}/img/p2.png").convert()

p3 = pygame.image.load(f"{phat}/img/p3.png").convert()

die = pygame.image.load(f"{phat}/img/die.png").convert()
die_r = die.get_rect(); die_r.y = 0; die_r.x = 0

frame = pygame.image.load(f"{phat}/img/frame.png").convert()
frame_r = frame.get_rect(); frame_r.y = 0; frame_r.x = 0

img = pygame.image.load(f"{phat}/img/img.png")
img_r = img.get_rect(); img_r.y = 100; img_r.x = 200




class game_state():
    def __init__(self):
        self.mode = 'menu'
        self.death = 0
        self.row1 = 100
        self.font = pygame.font.Font(f'{phat}/font/PixelDigivolve.ttf', 40)


    def menu(self):
        screen.blit(frame,frame_r)

        start = pygame.Rect(wid/2-125,330,250,80)
        quit = pygame.Rect(wid/2-125,430,250,80)

        pygame.draw.rect(screen,GREY,start,4)
        pygame.draw.rect(screen,GREY,quit,4)

        text = self.font.render('START', True, BLACK)
        screen.blit(text, (wid/2-65,340))

        text = self.font.render('QUIT', True, BLACK)
        screen.blit(text, (wid/2-45,440))

        test = pygame.Rect(wid/2-200,100,400,100)
        pygame.draw.rect(screen,RED,test,4)
        screen.blit(img,img_r)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if start.collidepoint(mouse):
                self.mode = 'lvl_select'
            if quit.collidepoint(mouse):
                save()
                pygame.quit()


    def lvl_select(self):
        screen.blit(frame,frame_r)

        button1 = pygame.Rect(100,self.row1,60,60)
        button2 = pygame.Rect(200,self.row1,60,60)
        button3 = pygame.Rect(300,self.row1,60,60)
        button4 = pygame.Rect(400,self.row1,60,60)
        button5 = pygame.Rect(500,self.row1,60,60)
        button6 = pygame.Rect(600,self.row1,60,60)
        
        pygame.draw.rect(screen,BLACK,button1,4)

        if mapp.done[0]:
            pygame.draw.rect(screen,GREEN,button2,4)
        else:
            pygame.draw.rect(screen,BLACK,button2,4)
        if mapp.done[1]:
            pygame.draw.rect(screen,GREEN,button3,4)
        else:
            pygame.draw.rect(screen,BLACK,button3,4)
        if mapp.done[2]:
            pygame.draw.rect(screen,GREEN,button4,4)
        else:
            pygame.draw.rect(screen,BLACK,button4,4)
        if mapp.done[3]:
            pygame.draw.rect(screen,GREEN,button5,4)
        else:
            pygame.draw.rect(screen,BLACK,button5,4)
        
        text = self.font.render('<-', True, BLACK)
        screen.blit(text, (110,self.row1+5))
        
        text = self.font.render('1', True, BLACK)
        screen.blit(text, (220,self.row1+5))

        text = self.font.render('2', True, BLACK)
        screen.blit(text, (320,self.row1+5))

        text = self.font.render('3', True, BLACK)
        screen.blit(text, (420,self.row1+5))
    
        text = self.font.render('4', True, BLACK)
        screen.blit(text, (520,self.row1+5))

    

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if button1.collidepoint(mouse):
                self.mode = 'menu'
            if button2.collidepoint(mouse):
                mapp.lvl = 1
                self.mode = 'game'
            if button3.collidepoint(mouse):
                mapp.lvl = 2
                self.mode = 'game'
            if button4.collidepoint(mouse):
                mapp.lvl = 3
                self.mode = 'game'
            if button5.collidepoint(mouse):
                mapp.lvl = 4
                self.mode = 'game'
            if button6.collidepoint(mouse):
                mapp.lvl = 5
                self.mode = 'game'


    def die(self):
        screen.blit(die,die_r)
        
        font = pygame.font.Font(f'{phat}/font/PixelDigivolve.ttf', 30)
        text = font.render(str(self.death), True, RED)
        screen.blit(text, (wid/2-60, 210))

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            character.x = 150
            character.y = 500
            self.mode = 'game'


    def game(self):
        #display
        mapp.draw()
        character.draw()


        if character.AI.colliderect(finish_r):
            mapp.done[mapp.lvl - 1] = True
            character.x = 150
            character.y = 500
            game.mode = 'lvl_select'
        
        
        self.mines = [mapp.m0,mapp.m1] 
        for i in range(len(self.mines)):
            if character.AI.colliderect(self.mines[i]):
                boom1_r.y = self.mines[i].y-50; boom1_r.x = self.mines[i].x-20; screen.blit(boom1,boom1_r)
                pygame.display.update()
                sleep(.1)
                boom2_r.y = self.mines[i].y-50; boom2_r.x = self.mines[i].x-20; screen.blit(boom2,boom2_r)
                pygame.display.update()
                sleep(.1)
                boom3_r.y = self.mines[i].y-50; boom3_r.x = self.mines[i].x-20; screen.blit(boom3,boom3_r)
                pygame.display.update()
                sleep(.5)
                self.death += 1
                game.mode = 'die'


        #player_input
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            character.right_left(.2)
        
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            character.right_left(-.2)

        character.jumps()

    
class block():
    def __init__(self,lvl,size):
        self.lvl = lvl
        self.size = size
        self.done = [False,False,False,False,False]
        self.flore = pygame.Rect(0,hig-size,wid,size)
        self.right_wall = pygame.Rect(0,0,size,hig)
        self.left_wall = pygame.Rect(wid-size,0,size,hig)

        self.b0 = pygame.Rect(0,-100,180,40)
        self.b1 = pygame.Rect(0,-100,180,40)
        self.b2 = pygame.Rect(0,-100,180,40)
        self.b3 = pygame.Rect(0,-100,180,40)
        self.b4 = pygame.Rect(0,-100,180,40)
        self.b5 = pygame.Rect(0,-100,180,40)

        self.m0 = pygame.Rect(0,-100,180,40)
        self.m1 = pygame.Rect(0,-100,180,40)


    def draw(self):
        screen.blit(border,border_r)
        background_r.y = 0; background_r.x = 60; screen.blit(background,background_r)
        finish_r.y = 0; finish_r.x = 60; screen.blit(finish,finish_r)

        if False:
            pygame.draw.rect(screen,GREEN,flore,0)
            pygame.draw.rect(screen,GREEN,right_wall,0)
            pygame.draw.rect(screen,GREEN,left_wall,0)


        #lvl number
        font = pygame.font.Font(f'{phat}/font/PixelDigivolve.ttf', 50)
        text = font.render(str(self.lvl), True, WHITE)
        screen.blit(text, (wid/2-20, 230))
    

        #level design
        match self.lvl:
            case 0:
                self.reset()


            case 1:
                self.reset()
                self.b0 = pygame.Rect(120,320,180,40)
                self.b1 = pygame.Rect(300,420,180,40)
                self.b2 = pygame.Rect(420,260,180,40)
                self.b3 = pygame.Rect(160,140,180,40)
                platform_r.x = 120; platform_r.y = 320; screen.blit(platform,platform_r)
                platform_r.x = 300; platform_r.y = 420; screen.blit(platform,platform_r)
                platform_r.x = 420; platform_r.y = 260; screen.blit(platform,platform_r)
                platform_r.x = 160; platform_r.y = 140; screen.blit(platform,platform_r)


            case 2:
                self.reset()
                self.b0 = pygame.Rect(120,320,180,40)
                self.b1 = pygame.Rect(300,420,180,40)
                self.b2 = pygame.Rect(420,260,180,40)
                self.b3 = pygame.Rect(160,140,180,40)
                platform_r.y = 320; platform_r.x = 120; screen.blit(platform,platform_r)
                platform_r.y = 420; platform_r.x = 300; screen.blit(platform,platform_r)
                platform_r.y = 260; platform_r.x = 420; screen.blit(platform,platform_r)
                platform_r.y = 140; platform_r.x = 160; screen.blit(platform,platform_r)
                if False:
                    pygame.draw.rect(screen,GREEN,self.b0,0)
                    pygame.draw.rect(screen,GREEN,self.b1,0)
                    pygame.draw.rect(screen,GREEN,self.b2,0)
                    pygame.draw.rect(screen,GREEN,self.b3,0)


                self.m1 = pygame.Rect(250,520,40,20)
                mine_r.x = 250; mine_r.y = 520; screen.blit(mine,mine_r)
    

            case 3:
                self.reset()
                self.b0 = pygame.Rect(160,420,180,40)
                self.b1 = pygame.Rect(400,340,180,40)
                self.b2 = pygame.Rect(500,260,180,40)
                self.b3 = pygame.Rect(280,150,180,40)
                platform_r.y = 420; platform_r.x = 160; screen.blit(platform,platform_r)
                platform_r.y = 340; platform_r.x = 400; screen.blit(platform,platform_r)
                platform_r.y = 260; platform_r.x = 500; screen.blit(platform,platform_r)
                platform_r.y = 150; platform_r.x = 280; screen.blit(platform,platform_r)


                self.m1 = pygame.Rect(300,400,40,20)
                mine_r.x = 300; mine_r.y = 400; screen.blit(mine,mine_r)


            case 4:
                self.reset()
                self.b0 = pygame.Rect(160,420,180,40)
                self.b1 = pygame.Rect(400,340,180,40)
                self.b2 = pygame.Rect(500,260,180,40)
                self.b3 = pygame.Rect(280,150,180,40)
                platform_r.y = 420; platform_r.x = 160; screen.blit(platform,platform_r)
                platform_r.y = 340; platform_r.x = 400; screen.blit(platform,platform_r)
                platform_r.y = 260; platform_r.x = 500; screen.blit(platform,platform_r)
                platform_r.y = 150; platform_r.x = 280; screen.blit(platform,platform_r)


                self.m1 = pygame.Rect(300,400,40,20)
                self.m0 = pygame.Rect(520,240,40,20)
                mine_r.x = 300; mine_r.y = 400; screen.blit(mine,mine_r)
                mine_r.x = 520; mine_r.y = 240; screen.blit(mine,mine_r)


    def reset(self):
        self.b0 = pygame.Rect(0,-100,180,40)
        self.b1 = pygame.Rect(0,-100,180,40)
        self.b2 = pygame.Rect(0,-100,180,40)
        self.b3 = pygame.Rect(0,-100,180,40)
        self.b4 = pygame.Rect(0,-100,180,40)
        self.b5 = pygame.Rect(0,-100,180,40)

        self.m0 = pygame.Rect(0,-100,180,40)
        self.m1 = pygame.Rect(0,-100,180,40)


class player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wid = 40
        self.hig = 40
        
        self.max_jump = 4
        self.max_speed = 1
        self.h_vel = 0
        self.v_vel = 0
        self.power = 0
        self.jump = False
        self.object_list = []
        self.colliders = []
        self.collide = False
        self.skin = [p0,p1,p2,p3]


    def draw(self):
        self.AI = pygame.Rect(self.x, self.y ,40 ,40)

        player_r.y = self.y; player_r.x = self.x; screen.blit(self.skin[0],player_r)

        if False:
            pygame.draw.rect(screen, WHITE, self.AI, 0)

        #player name
        font = pygame.font.Font(f'{phat}/font/PixelDigivolve.ttf', 20)
        text = font.render('player', True, ORANGE)
        screen.blit(text, (self.x - 20, self.y - 30))


        #jump power
        self.box = pygame.Rect(70, 555 ,110 ,20)
        pygame.draw.rect(screen, BLACK, self.box, 1)

        self.line = pygame.Rect(75, 560 ,(self.power / self.max_jump) * 100 ,10)
        pygame.draw.rect(screen, RED, self.line, 0)



    def right_left(self,speed):
        self.h_vel += speed
        self.h_vel = round(self.h_vel,2)
        if self.h_vel != 0:
            if self.h_vel >= self.max_speed:
                self.h_vel = self.max_speed
            if self.h_vel <= -self.max_speed:
                self.h_vel = -self.max_speed
        if self.h_vel > 0 and self.h_vel != 0:
            self.h_vel -= .05
        if self.h_vel < 0 and self.h_vel != 0:
            self.h_vel += .05
        self.x += self.h_vel
        if self.x > 700:
            self.x = 700
        if self.x < 80:
            self.x = 80
        

        
    def jumps(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.jump = True
        else:
            self.jump = False
        self.object_list = [mapp.b0,mapp.b1,mapp.b2,mapp.b3,mapp.b4,mapp.b5]
        self.collide = False
        self.colliders = []
        for i in range(len(self.object_list)):
            if self.AI.colliderect(self.object_list[i]):
                
                self.collide = True
                self.colliders.append(self.object_list[i])
        if self.collide:
            self.v_vel = 0
            for j in range(len(self.colliders)):
                if self.x < self.colliders[j].x - 35:
                    self.x -= 1
                if self.x > self.colliders[j].x + 175:
                    self.x += 1
                if self.y < self.colliders[j].y + 60 and not self.y < self.colliders[j].y:
                    self.y += .1
        if self.jump:
            self.power += .02    
        if self.power > self.max_jump:
            self.power = self.max_jump
        if (not self.jump) and self.power > 0:
            self.v_vel = self.power * -1
            self.power = 0
        self.v_vel = round(self.v_vel,2) 
        if self.v_vel > 0 and self.v_vel != 0:
            self.v_vel -= .05
        if self.v_vel < 0 and self.v_vel != 0:
            self.v_vel += .05
        self.y += self.v_vel
        #gravity/physics
        if not self.collide:
            if self.v_vel >= 0:
                self.v_vel += .1
            if self.v_vel > self.max_jump:
                self.v_vel = self.max_jump
        if self.y > 500:
            self.y = 500     


def save():
    #saving mechanic
    pass


character = player(wid/2-20,500)
mapp = block(1,60)
game = game_state()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #key input
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        game.mode = 'lvl_select'
        character.x = 150
        character.y = 500
    if key[pygame.K_d]:
        print(mapp.done)

    match game.mode:
        case 'game':
            game.game()
        case 'die':
            game.die()
        case 'menu':
            game.menu()
        case 'lvl_select':
            game.lvl_select()


    pygame.display.update()
    #pygame.display.flip()
save()
pygame.quit()


'''

#4:1 px ratio


'''