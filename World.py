from random import randrange

import pygame

from configs import *
from DataGame import DataScore


class ObstacleOptions:
    STUB = 0
    FLY = 1
    SNAKE = 2

class GameStatus:
    def __init__(self):
        self.__isGameOver = False
        self.__gameOverSound = pygame.mixer.Sound('sounds/gameover.wav')
        self.__score = 0
        self.__highScore = DataScore().hiScore()
        self.__speedLevel = 10
        self.__levelSound = pygame.mixer.Sound('sounds/level_up.wav')
        self.__isWaitingRestart = False

    def getScore(self):
        return self.__score

    def getGameOverState(self):
        return self.__isGameOver

    def getHighScore(self):
        return self.__highScore

    def getWaitingRestart(self):
        return self.__isWaitingRestart

    def getSpeedLevel(self):
        return self.__speedLevel

    def updateScore(self):
        self.__score += 1

    def resetState(self):
        self.__score = 0
        self.__speedLevel = 10

    def setGameOverState(self, newState):
        if newState:
            self.__gameOverSound.play()
            DataScore().hiScore(self.__score)

        self.__isGameOver = newState

    def setWaitingRestart(self, newState):
        self.__isWaitingRestart = newState
    
    def updateSpeedLevel(self):
        self.__speedLevel += 1
        self.__levelSound.play()

    def updateHighScore(self):
        if self.__score > self.__highScore:
            self.__highScore = self.__score


class Floor(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imgs/assets/floor.png")
        self.rect = self.image.get_rect()
        self.rect.y = HEIGHT - 100
        self.rect.x = pos_x * 950 
        self.__speed = GameStatus()

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = WIDTH
        self.rect.x -= self.__speed.getSpeedLevel()


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imgs/assets/trees.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH,  460)
        self.rect.x = pos_x * 960
        self.__speed = GameStatus()

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = WIDTH
        self.rect.x -= 5

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imgs/assets/cloud.png")
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 250, 25)
        self.rect.x = WIDTH - randrange(30, 800, 40)
        self.__speed = GameStatus()

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = WIDTH
            self.rect.y = randrange(50, 200, 50)
        self.rect.x -= 3

class Mountain(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imgs/assets/montain.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH,  500)
        self.rect.x = pos_x * 878
        self.__speed = GameStatus()

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = WIDTH
        self.rect.x -= 2

class ResetAssets:
    def __init__(self, assets):
        for element in assets:
            element.rect.x = WIDTH

class GameAlert:
    def __init__(self, surface, txt, size, color, position):
        self.__font = pygame.font.Font('fonts/PixelEmulator-xq08.ttf', size)
        self.__txt = self.__font.render(txt, True, color)
        self.__alet = surface.blit(self.__txt, position)

