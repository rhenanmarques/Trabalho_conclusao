import pygame
from configs import *
from World import GameStatus, ObstacleOptions

class Stub(pygame.sprite.Sprite):
    def __init__(self, chosenOption):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imgs/assets/stub-s.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (WIDTH, HEIGHT - 60)
        self.rect.x = WIDTH
        self.__chosenOption = chosenOption
        self.__speed = GameStatus()

    def update(self):
        if self.__chosenOption == ObstacleOptions.STUB:
            if self.rect.topright[0] < 0:
                self.rect.x = WIDTH
            self.rect.x -= self.__speed.getSpeedLevel()

    def setChosen(self, chosenOption):
        self.__chosenOption = chosenOption

    def getRectTopRight(self):
        return self.rect.topright[0]
        

class Flying(pygame.sprite.Sprite):
    def __init__(self, chosenOption):
        pygame.sprite.Sprite.__init__(self)
        self.__sprite_sheet = pygame.image.load("imgs/enemy/fly_sprite.png")
        self.__sprites = []
        for i in range(8):
            img = self.__sprite_sheet.subsurface((i * 74, 0), (74, 60))
            self.__sprites.append(img)
        self.__spriteIndex = 0
        self.image = self.__sprites[self.__spriteIndex]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (WIDTH, 540)
        self.rect.x = WIDTH
        self.__chosenOption = chosenOption
        self.__speed = GameStatus()

    def getRectTopRight(self):
        return self.rect.topright[0]

    def update(self):
        if self.__chosenOption == ObstacleOptions.FLY:
            if self.rect.topright[0] < 0:
                self.rect.x = WIDTH
            self.rect.x -= self.__speed.getSpeedLevel()

            if self.__spriteIndex > 7:
                self.__spriteIndex = 0
            self.__spriteIndex += 0.25
            self.image = self.__sprites[int(self.__spriteIndex)]

    def setChosen(self, newChosenOption):
        self.__chosenOption = newChosenOption

class Snake(pygame.sprite.Sprite):
    def __init__(self, chosenOption):
        pygame.sprite.Sprite.__init__(self)
        self.__sprite_sheet = pygame.image.load("imgs/enemy/snake_sprite.png")
        self.__sprites = []
        for i in range(10):
            img = self.__sprite_sheet.subsurface((i * 85, 0), (85, 90))
            self.__sprites.append(img)
        self.__spriteIndex = 0
        self.image = self.__sprites[self.__spriteIndex]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (WIDTH, HEIGHT - 80)
        self.rect.x = WIDTH
        self.__chosenOption = chosenOption
        self.__speed = GameStatus()

    def getRectTopRight(self):
        return self.rect.topright[0]

    def update(self):
        if self.__chosenOption == ObstacleOptions.SNAKE:
            if self.rect.topright[0] < 0:
                self.rect.x = WIDTH
            self.rect.x -= self.__speed.getSpeedLevel()

            if self.__spriteIndex > 9:
                self.__spriteIndex = 0
            self.__spriteIndex += 0.35
            self.image = self.__sprites[int(self.__spriteIndex)]

    def setChosen(self, newChosenOption):
        self.__chosenOption = newChosenOption
