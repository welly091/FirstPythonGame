import pygame
import random

FPS = 60
WHITE = (255,255,255)
WIDTH = 500
HEIGHT = 600

# Initiate the game and create a window
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__((self))
        self.image = pygame.Surface((50,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT-10
        self.speedx = 4

    def update(self):
        #Check if arrow keys are pressed
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_a]:
            self.rect.x -= self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__((self))
        self.image = pygame.Surface((30,40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(2,8)
        self.speedx = random.randrange(-3,3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 8)
            self.speedx = random.randrange(-3, 3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__((self))
        self.image = pygame.Surface((10, 20))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10


    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    rock = Rock()
    all_sprites.add(rock)

running = True

#Game loop!
while running:
    #Only run FPS times per seconds
    clock.tick(FPS)
    #Entry
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    #Update the game
    all_sprites.update()

    #Reveal to game background
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()