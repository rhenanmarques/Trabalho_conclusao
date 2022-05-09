import pygame

from configs import *


class Player (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.__sprite_sheet = pygame.image.load(
            "imgs/player/Player_spritesheet.png")
        self.__sprites = []
        for i in range(8):
            img = self.__sprite_sheet.subsurface((i * 142, 0), (142, 120))
            self.__sprites.append(img)
        self.__spriteIndex = 0
        self.image = self.__sprites[self.__spriteIndex]
        self.rect = self.image.get_rect()
        self.__imgJump = self.__sprite_sheet.subsurface((8 * 142, 0), (142, 120))
        self.__imgSlide = self.__sprite_sheet.subsurface((9 * 142, 0), (142, 120))
        self.mask = pygame.mask.from_surface(self.image)
        self.__floorY = HEIGHT - 110 - 96 // 2
        self.rect.topleft = (100, self.__floorY)
        self.__isJumping = False
        self.__jumpSound = pygame.mixer.Sound('sounds/jump.wav')
        self.__isSlide = False

    def jump(self):
        if self.rect.y != self.__floorY:
            return

        if not self.__isJumping:
            self.__isJumping = True
            self.__jumpSound.play()

    def slide(self):
        if not self.__isSlide and self.rect.y == self.__floorY:
            self.__isSlide = True

    def update(self):
        if self.__spriteIndex > 7:
            self.__spriteIndex = 0
        self.__spriteIndex += 0.75
        self.image = self.__sprites[int(self.__spriteIndex)]

        if self.__isJumping:
            self.image = self.__imgJump
            if self.rect.y <= self.__floorY - 150:
                self.__isJumping = False
            self.rect.y -= 15
        else:
            if self.rect.y >= self.__floorY:
                self.rect.y = self.__floorY
            else:
                self.rect.y += 15

        if self.__isSlide:
            self.image = self.__imgSlide
            self.mask = pygame.mask.from_surface(self.image).scale((97, 86))
            self.__isSlide = False
        elif not self.__isSlide:
            self.mask = pygame.mask.from_surface(self.image)

    def resetPosition(self):
        self.rect.y = self.__floorY
        self.__isJumping = False
