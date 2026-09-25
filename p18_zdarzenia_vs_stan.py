"""Przykład 18: ruch na zdarzeniach kontra ruch na stanie klawiszy."""
import pygame

SZEROKOSC, WYSOKOSC = 800, 400
FPS = 60
TLO = (28, 28, 40)
ZLY = (220, 80, 80)
DOBRY = (110, 200, 120)
PREDKOSC = 300  
SKOK = 5      

pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Zdarzenia kontra stan - steruj strzalkami")
zegar = pygame.time.Clock()
czcionka = pygame.font.Font(None, 26)

zly = pygame.Rect(100, 90, 50, 50)
dobry_x = 100.0
dobry = pygame.Rect(100, 250, 50, 50)

dziala = True
while dziala:

    dt = zegar.tick(FPS) / 1000.0


    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                dziala = False
            elif zdarzenie.key == pygame.K_LEFT:
                zly.x -= SKOK
            elif zdarzenie.key == pygame.K_RIGHT:
                zly.x += SKOK

    klawisze = pygame.key.get_pressed()
    if klawisze[pygame.K_LEFT]:
        dobry_x -= PREDKOSC * dt
    if klawisze[pygame.K_RIGHT]:
        dobry_x += PREDKOSC * dt
    
    dobry.x = int(dobry_x)


    ekran.fill(TLO)
    
    pygame.draw.rect(ekran, ZLY, zly)
    pygame.draw.rect(ekran, DOBRY, dobry)
    
    ekran.blit(czcionka.render("ZDARZENIE (KEYDOWN): rusza sie skokowo", True, ZLY), (20, 40))
    ekran.blit(czcionka.render("STAN (get_pressed): plynnie, dopoki trzymasz", True, DOBRY), (20, 200))
    
    pygame.display.flip()

pygame.quit()
