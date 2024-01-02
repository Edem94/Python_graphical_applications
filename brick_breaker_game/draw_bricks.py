import pygame

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brick Breaker Game")
floor = pygame.Rect(100, 550, 200, 10)
ball = pygame.Rect(50, 250, 10, 10)
score = 0
move = [1, 3]

GREEN = (28, 252, 106)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (252, 3, 152)
ORANGE = (252, 170, 28)
RED = (255, 0, 0)

# bricks
b1 = [pygame.Rect(1 + i * 100, 60, 98, 38) for i in range(6)]
b2 = [pygame.Rect(1 + i * 100, 100, 98, 38) for i in range(6)]
b3 = [pygame.Rect(1 + i * 100, 140, 98, 38) for i in range(6)]


# Draw bricks on screen
def draw_brick(bricks):
    for i in bricks:
        pygame.draw.rect(screen, ORANGE, i)
