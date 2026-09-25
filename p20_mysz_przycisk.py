import pygame

SZEROKOSC, WYSOKOSC = 700, 460
FPS = 60
TLO = (28, 28, 40)
ZWYKLY = (60, 90, 150)
NAJECHANY = (85, 125, 200)
WCISNIETY = (40, 62, 105)
NAPIS = (240, 240, 245)

pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Mysz i przyciski")
zegar = pygame.time.Clock()
czcionka = pygame.font.Font(None, 30)
male = pygame.font.Font(None, 24)

PRZYCISKI = [
    (pygame.Rect(0, 0, 240, 64), "Nowa gra"),
    (pygame.Rect(0, 0, 240, 64), "Wyniki"),
    (pygame.Rect(0, 0, 240, 64), "Wyjscie"),
]

for i, (prostokat, _) in enumerate(PRZYCISKI):
    prostokat.center = (SZEROKOSC // 2, 130 + i * 90)

komunikat = "Kliknij przycisk"

def rysuj_przycisk(ekran, prostokat, napis, najechany, wcisniety):
    """Rysuje przycisk w jednym z trzech stanów."""
    if wcisniety:
        kolor, przesun = WCISNIETY, 2
    elif najechany:
        kolor, przesun = NAJECHANY, 0
    else:
        kolor, przesun = ZWYKLY, 0
        
    pygame.draw.rect(ekran, kolor, prostokat, 0, 10)
    
    if najechany:
        pygame.draw.rect(ekran, NAPIS, prostokat, 2, 10)
        
    tekst = czcionka.render(napis, True, NAPIS)
    ekran.blit(tekst, tekst.get_rect(center=(prostokat.centerx, prostokat.centery + przesun)))

dziala = True
while dziala:
    zegar.tick(FPS)
    mysz = pygame.mouse.get_pos()
    lewy_wcisniety = pygame.mouse.get_pressed()[0]
    
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_ESCAPE:
            dziala = False
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
            for prostokat, napis in PRZYCISKI:
                if prostokat.collidepoint(zdarzenie.pos):
                    komunikat = f"Kliknieto: {napis}"
                    if napis == "Wyjscie":
                        dziala = False
                        
    ekran.fill(TLO)
    
    for prostokat, napis in PRZYCISKI:
        najechany = prostokat.collidepoint(mysz)
        rysuj_przycisk(ekran, prostokat, napis, najechany, najechany and lewy_wcisniety)
        
    ekran.blit(male.render(f"kursor: {mysz}", True, (150, 150, 165)), (20, 20))
    ekran.blit(male.render(komunikat, True, (200, 200, 215)), (20, WYSOKOSC - 40))
    
    pygame.display.flip()

pygame.quit()
