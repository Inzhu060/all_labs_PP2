import pygame, sys, os, random, time
from pygame.locals import *

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# FPS settings
FPS = 60
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Screen and game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# Fonts
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font_big.render("Game Over", True, BLACK)

# Load resources
background = pygame.image.load("AnimatedStreet.png")
player_image = pygame.image.load("Player.png")
enemy_image = pygame.image.load("Enemy.png")
coin_image = pygame.image.load("coin.png")
coin_image = pygame.transform.scale(coin_image, (30, 30))

# Load sound
if os.path.exists("coin_sound.wav"):
    coin_sound = pygame.mixer.Sound("coin_sound.wav")
    coin_sound.set_volume(1.0)
else:
    print("coin_sound.wav not found")
    coin_sound = None

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

#SPRITE CLASSES

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0 and keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, enemies_group):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()

        # Try to spawn coin away from enemies
        while True:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            too_close = False
            for enemy in enemies_group:
                if self.rect.colliderect(enemy.rect.inflate(60, 100)):
                    too_close = True
                    break
            if not too_close:
                break

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#SETUP SPRITES

P1 = Player()
E1 = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E1)

C1 = Coin(enemies)
coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Speed increase event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#MAIN GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Background
    screen.blit(background, (0, 0))

    # Display score and coins
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    # Move and draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Check for collision with enemy (Game Over)
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over_text, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check for coin collection
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        if coin_sound:
            coin_sound.play()
        for coin in coins:
            coin.kill()
            new_coin = Coin(enemies)
            coins.add(new_coin)
            all_sprites.add(new_coin)

    # Update display
    pygame.display.update()
    clock.tick(FPS)