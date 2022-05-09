import pygame
import pygame.locals
from Obstacle import *
from Player import Player
from World import *
from configs import *
from random import choice

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
title = pygame.display.set_caption("Trabalho de conclusão de Curso")#type: ignore
ico = pygame.image.load("imgs/ico.ico")
ico = pygame.display.set_icon(ico)#type: ignore
clock = pygame.time.Clock()
skyColor = (226,234,252)

#sound
pygame.mixer.init()

#sprites
spritesToDraw = pygame.sprite.Group()
#--world
for mount in range(WIDTH * 3 // 878):
    mountain = Mountain(mount)
    spritesToDraw.add(mountain)

for t in range(WIDTH * 3 // 960):
    tree = Tree(t)
    spritesToDraw.add(tree)

for grd in range(WIDTH * 3 // 950):
    ground = Floor(grd)
    spritesToDraw.add(ground)

for clou in range(3):
    cloud = Cloud()
    spritesToDraw.add(cloud)

#--char
p1 = Player()
spritesToDraw.add(p1)

#--obstacle

obstacles = pygame.sprite.Group()
obstacleToDisplay = choice([ObstacleOptions.STUB, ObstacleOptions.FLY, ObstacleOptions.SNAKE])

stub = Stub(obstacleToDisplay)
spritesToDraw.add(stub)
obstacles.add(stub)

flyEnemy = Flying(obstacleToDisplay)
spritesToDraw.add(flyEnemy)
obstacles.add(flyEnemy)

snakeEnemy = Snake(obstacleToDisplay)
spritesToDraw.add(snakeEnemy)
obstacles.add(snakeEnemy)


#Game Status
gameStatus = GameStatus() 
exit = False

while not exit:
    #FPS
    clock.tick(30)

    #exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    #GameOver
    if gameStatus.getGameOverState():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            gameStatus.setGameOverState(False)
            gameStatus.resetState()
            ResetAssets((stub, flyEnemy, snakeEnemy))
            p1.resetPosition()
            gameStatus.setWaitingRestart(False)
            obstacleToDisplay = choice([ObstacleOptions.STUB, ObstacleOptions.FLY, ObstacleOptions.SNAKE])
            continue
            
        GameAlert(screen, "Game Over", 45, 'black', (250, 250))
        GameAlert(screen, f"Score: {gameStatus.getScore()} High Score: {gameStatus.getHighScore()}", 24, 'black', (180, 300))
        GameAlert(screen, "Pressione R para jogar novamente", 18, 'black', (190, 330))
        pygame.display.update()

        if not gameStatus.getWaitingRestart():
            gameStatus.setWaitingRestart(True)

        pygame.display.update()
        continue

    #Teclado
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        p1.jump()
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        p1.slide()

    #draw elements
    screen.fill(skyColor)
    spritesToDraw.draw(screen)

    if stub.getRectTopRight() <= 0 or flyEnemy.getRectTopRight() <= 0 or snakeEnemy.getRectTopRight() <= 0:
        obstacleToDisplay = choice([ObstacleOptions.STUB, ObstacleOptions.FLY, ObstacleOptions.SNAKE])
        for asset in (stub, flyEnemy, snakeEnemy):
            asset.rect.x = WIDTH #type: ignore
            asset.setChosen(obstacleToDisplay) #type: ignore

    #colides
    colides = pygame.sprite.spritecollide(p1, obstacles, False, pygame.sprite.collide_mask)# type: ignore

    if colides:
        gameStatus.setGameOverState(True)

    else:
        gameStatus.updateScore()
        gameStatus.updateHighScore()
        spritesToDraw.update()
        GameAlert(screen, f"Score: {gameStatus.getScore()}", 18, 'black', (10, 10))
        GameAlert(screen, f"High Score: {gameStatus.getHighScore()}", 18, 'black', (250, 10))
        GameAlert(screen, f"UP ou W - Pular", 16, "white", (10, HEIGHT - 30))
        GameAlert(screen, f"DOWN ou S - Deslizar", 16, "white", (250, HEIGHT - 30))
    
    if gameStatus.getScore() % 100 == 0:
        gameStatus.updateSpeedLevel()
 
    pygame.display.update()
    
pygame.quit()