import pygame
import random


class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load("images/apple.png")
        losowa_pozycja = pygame.Rect(
            random.randrange(0, 24) * 32, random.randrange(0, 18) * 32, 32, 32
        )
        self.pozycja = losowa_pozycja
