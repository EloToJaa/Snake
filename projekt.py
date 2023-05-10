# Importy
import pygame
import random
import time
from Jablko import Jablko
from Kierunek import Kierunek
from Waz import Waz

# Stałe
SZEROKOSC_KAFELKI = 25
WYSOKOSC_KAFELKI = 19
SZEROKOSC_EKRANU = SZEROKOSC_KAFELKI * 32
WYSOKOSC_EKRANU = WYSOKOSC_KAFELKI * 32
FPS = 60
PORUSZ_WEZEM = pygame.USEREVENT + 1

# Tworzenie tła
tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))

for i in range(SZEROKOSC_KAFELKI):
    for j in range(WYSOKOSC_KAFELKI):
        obraz = pygame.image.load("images/background.png")
        maska = (
            random.randrange(0, 20),
            random.randrange(0, 20),
            random.randrange(0, 20),
        )

        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        tlo.blit(obraz, (i * 32, j * 32))

# Start
pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))
zegar = pygame.time.Clock()

# Wąż
waz = Waz()
pygame.time.set_timer(PORUSZ_WEZEM, 150)

# Jabłka
jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)

# Pętla gry
gra_dziala = True
while gra_dziala:
    # Zdarzenia
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gra_dziala = False
            if event.key == pygame.K_w:
                waz.zmien_kierunek(Kierunek.GORA)
            if event.key == pygame.K_s:
                waz.zmien_kierunek(Kierunek.DOL)
            if event.key == pygame.K_a:
                waz.zmien_kierunek(Kierunek.LEWO)
            if event.key == pygame.K_d:
                waz.zmien_kierunek(Kierunek.PRAWO)

        elif event.type == pygame.QUIT:
            gra_dziala = False
        elif event.type == PORUSZ_WEZEM:
            waz.aktualizuj()

    # Rysowanie
    ekran.blit(tlo, (0, 0))
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.pozycja)
    ekran.blit(waz.obraz, waz.pozycja)

    # Koniec pętli
    pygame.display.flip()
    zegar.tick(FPS)

# Koniec
time.sleep(1)
pygame.quit()
