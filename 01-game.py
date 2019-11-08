import pygame, random
pygame.init()

WIDTH = 600
HEIGHT = 250
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
RANDOM_COLOR = 87,54,98
x = 0
y = 25
moveX = 0
moveY = 0
x2 = random.randint(0, WIDTH - 50)
y2 = random.randint(0, HEIGHT - 50)
frog = pygame.image.load('assets/frog.png')
sound = pygame.mixer.Sound('assets/point.wav')
counter = 0
SNAKE_WIDTH = 50
fps = 50
snakeLength = 1
clock = pygame.time.Clock()

snakeList = []

gameBoard = pygame.display.set_mode((WIDTH,HEIGHT))

def displayScore():
    msg = f'Score : {counter}'
    font = pygame.font.SysFont(None, 30, True, True)
    score = font.render(msg, True, RANDOM_COLOR)
    gameBoard.blit(score, (0,0))

def drawSnake():
    for bodyPart in snakeList:
        pygame.draw.rect(gameBoard, RED, (bodyPart[0], bodyPart[1], 50,50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moveY = -1
                moveX = 0
            elif event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0

    gameBoard.fill( WHITE )
    #rect1 = pygame.draw.rect(gameBoard, RED, (x,y,SNAKE_WIDTH,50))
    rect1 = pygame.Rect( (x , y , 50 , 50) )
    #rect2 = pygame.draw.rect(gameBoard, WHITE, (x2,y2,50,50))
    gameBoard.blit(frog, (x2,y2))
    rect2 = pygame.Rect((x2,y2,50,50))

    snakeHead = [x,y]
    snakeList.append(snakeHead)
    if len(snakeList) > snakeLength:
        del snakeList[0]
    print(snakeList)
    drawSnake()

    displayScore()

    if rect1.colliderect(rect2):
        x2 = random.randint( 0 , WIDTH - 50 )
        y2 = random.randint( 0 , HEIGHT - 50 )
        sound.play()
        counter += 1
        #SNAKE_WIDTH += 10
        fps += 10
        snakeLength += 10

    x += moveX
    y += moveY

    if x > WIDTH:
        x = -50
    elif x < -50:
        x = WIDTH
    elif y > HEIGHT:
        y = -50
    elif y < -50:
        y = HEIGHT

    # if y > HEIGHT - 50:
    #     moveY = -1
    # elif y < 0:
    #     moveY = 1
    # elif x > WIDTH - 50:
    #     moveX = -1
    # elif x < 0:
    #     moveX = 1

    pygame.display.update()
    clock.tick(fps)