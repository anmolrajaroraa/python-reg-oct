import pygame
import random
pygame.init()

HEIGHT = 500
WIDTH = 1000
BLACK = 0,0,0
WHITE = 255,255,255
RANDOM_COLOR = 100,150,200
RED = 255,0,0
X = 0
Y = 0
fps = 250
moveX = 1
moveY = 1
clock = pygame.time.Clock()
gameboard = pygame.display.set_mode((WIDTH, HEIGHT))
while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0

    gameboard.fill(WHITE)

    #screen, color, (x,y,width,height)
    # pygame.draw.rect(gameboard, RED, (X,Y,50,50))
    pygame.draw.circle(gameboard, RANDOM_COLOR, (X,Y), 50)
    # X = random.randint(0,950)
    # Y = random.randint(0,450)
    X += moveX
    Y += moveY

    if Y > HEIGHT - 50:
        moveY = -1
    elif Y < 0:
        moveY = 1
    elif X > WIDTH - 50:
        moveX = -1
    elif X < 0 :
        moveX = 1
    pygame.display.update()
    clock.tick(fps)
