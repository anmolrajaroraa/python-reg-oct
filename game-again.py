import pygame
pygame.init()

HEIGHT = 500
WIDTH = 1000
# red green blue (0-255)
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
RANDOM_COLOR = 100,150,200
gameboard = pygame.display.set_mode((WIDTH,HEIGHT))

while True:
    print("!")
    gameboard.fill( BLACK )
    pygame.display.update( )
