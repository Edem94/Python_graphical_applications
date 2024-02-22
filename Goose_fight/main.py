import os
import pygame
import random
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

# set screen size
HEIGHT = 800
WIDTH = 1200

# set color's values
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)

# set font for score text
FONT = pygame.font.SysFont("Verdana", 20)
FPS = pygame.time.Clock()

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

#background animation
bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

IMAGE_PATH = "Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

# Player creation
player_size = (20, 20)
player = pygame.image.load('player.png').convert_alpha()
player_rect = player.get_rect()
player_rect.center = main_display.get_rect().center

# set player movement
player_move_down = [0, 4]
player_move_right = [4, 0]
player_move_up = [0, -4]
player_move_left = [-4, 0]

# enemy creation
def create_enemy():
    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy_height = enemy.get_height()
    enemy_rect = pygame.Rect(WIDTH, 
                            random.randint(enemy_height, HEIGHT - enemy_height), 
                            *enemy.get_size())
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]

# bonus creation
def create_bonus():
    bonus = pygame.image.load('bonus.png').convert_alpha()
    bonus_width = bonus.get_width()
    bonus_rect = pygame.Rect(random.randint(bonus_width, WIDTH - bonus_width), 
                             -bonus.get_height(), 
                             *bonus.get_size())
    bonus_move = [0, random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

enemies = []
bonuses = []
score = 0

playing = True

# main game loop
while playing:
    FPS.tick(180)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()
    
    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    keys = pygame.key.get_pressed()

    # player movement using keyboard
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    # enemies display on the screen
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
            playing = False

    # bonus display and movement on the screen
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))

    # score display
    main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH-50, 20))
    main_display.blit(player, player_rect)

    pygame.display.flip()

    # Only relevant enemies remain in the list
    for enemy in enemies:
        if enemy[1].right < 0:
            enemies.pop(enemies.index(enemy))

     # Only relevant bonuses remain in the list
    for bonus in bonuses:
        if bonus[1].top > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
