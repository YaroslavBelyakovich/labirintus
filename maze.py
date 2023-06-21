from pygame import * 

class GameSprite(sprite.Sprite):
    def __init__(self, image_sprite, img_x,img_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_sprite), (65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x =  img_x
        self.rect.y = img_y

    def show_s(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width -80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_hight - 80:
            self.rect.y += self.speed

class   Enemy(GameSprite):
    naprav = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.naprav = 'right'
        if self.rect.x >= win_width - 85:
            self.naprav = 'left'

        if self.naprav == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,color1,color2,color3,wall_x,wall_y,wall_width,wall_hight):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.wall_width = wall_width
        self.wall_hight = wall_hight

        self.image = Surface ((self.wall_width, self.wall_hight))
        self.image.fill((self.color1,self.color2,self.color3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def show_s(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

    


win_width = 700
win_hight = 500

window = display.set_mode((win_width,win_hight))
display.set_caption('Лабирин')

background = transform.scale(image.load('background.jpg'),(win_width,win_hight))

player = Player('hero.png',5, win_hight-70,4)
monstr = Enemy('cyborg.png',win_width - 80,280,2)
finish_s = GameSprite('treasure.png',win_width-120,win_hight-80,0)
game = True
finish = False

w1 = Wall(147,234,12,220,340,10,300)
w2 = Wall(147,234,12,310,10,10,340)
w3 = Wall(147,234,12,400,340,10,300)

clock = time.Clock()

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

font.init()
font = font.Font(None,70)
win = font.render('YOU WIN!',True,(250,215,0))
lose = font.render('YOU LOSE!',True,(180,0,0))

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        player.show_s()
        monstr.show_s()
        finish_s.show_s()
        w1.show_s()
        w2.show_s()
        w3.show_s()

        if sprite.collide_rect(player,monstr) or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3):
            finish = True
            window.blit(lose,(200,200))

        if sprite.collide_rect(player,finish_s):
            finish = True
            window.blit(win,(200,200))

        player.update()
        monstr.update()

    display.update()
    clock.tick(60)













