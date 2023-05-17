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

# Punkty
punkty = 0

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
moja_czcionka = pygame.font.SysFont("Comic Sans MS", 24)

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

    # Kolizje
    kolizja_z_jablkiem = pygame.sprite.spritecollideany(waz, jablka)
    if kolizja_z_jablkiem != None:
        kolizja_z_jablkiem.kill()
        waz.jedz_jablko()
        jablko = Jablko()
        jablka.add(jablko)
        punkty += 1

    # Rysowanie
    ekran.blit(tlo, (0, 0))
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)
    ekran.blit(waz.obraz, waz.rect)
    waz.rysuj_segmenty(ekran)

    # Tekst
    tekst_z_wynikiem = moja_czcionka.render(f"Wynik: {punkty}", False, (0, 0, 0))
    ekran.blit(tekst_z_wynikiem, (16, 16))

    # Kolizje
    if waz.sprawdz_kolizje():
        gra_dziala = False
        tekst_z_przegrana = moja_czcionka.render("Przegrana", False, (200, 0, 0))
        ekran.blit(tekst_z_przegrana, (SZEROKOSC_EKRANU / 2 - 50, WYSOKOSC_EKRANU / 2))

    # Koniec pętli
    pygame.display.flip()
    zegar.tick(FPS)

# Koniec
time.sleep(1)
pygame.quit()
