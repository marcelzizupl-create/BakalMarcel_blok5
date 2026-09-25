import math
import pygame

SZEROKOSC, WYSOKOSC = 800, 500
FPS = 60
TLO = (28, 28, 40)
GRACZ = (90, 150, 240)
SLAD = (60, 70, 100)
PREDKOSC = 260
MNOZNIK_BIEGU = 2.0

pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Osiem kierunkow")
zegar = pygame.time.Clock()
czcionka = pygame.font.Font(None, 24)
EKRAN = pygame.Rect(0, 0, SZEROKOSC, WYSOKOSC)

x, y = 400.0, 250.0
gracz = pygame.Rect(0, 0, 44, 44)
poprawka_skosu = True
slad = []
dziala = True

while dziala:
    dt = zegar.tick(FPS) / 1000
    
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                dziala = False
            elif zdarzenie.key == pygame.K_TAB:
                poprawka_skosu = not poprawka_skosu

    klawisze = pygame.key.get_pressed()
    dx = 0.0
    dy = 0.0

    if klawisze[pygame.K_LEFT]:
        dx -= 1
    if klawisze[pygame.K_RIGHT]:
        dx += 1
    if klawisze[pygame.K_UP]:
        dy -= 1
    if klawisze[pygame.K_DOWN]:
        dy += 1

    if poprawka_skosu and dx != 0 and dy != 0:
        dx /= math.sqrt(2)
        dy /= math.sqrt(2)

    predkosc = PREDKOSC
    if klawisze[pygame.K_LSHIFT]:
        predkosc *= MNOZNIK_BIEGU

    x += dx * predkosc * dt
    y += dy * predkosc * dt
    
    gracz.center = (x, y)
    gracz.clamp_ip(EKRAN)
    x, y = gracz.center

    if dx != 0 or dy != 0:
        slad.append(gracz.center)
    if len(slad) > 120:
        slad.pop(0)

    ekran.fill(TLO)
    
    for punkt in slad:
        pygame.draw.circle(ekran, SLAD, punkt, 3)
        
    pygame.draw.rect(ekran, GRACZ, gracz, 0, 8)
    
    stan = "wlaczona" if poprawka_skosu else "WYLACZONA"
    ekran.blit(czcionka.render(f"Poprawka skosu: {stan} (TAB przelacza)", True, (235, 235, 230)), (20, 20))
    
    pygame.display.flip()

pygame.quit()
