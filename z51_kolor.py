import pygame
#Zdarzenie bo jak klikkam to się zmeinia kolor tła
SZEROKOSC, WYSOKOSC = 800, 600
FPS = 60
TLO = (28, 28, 40)
TLOCZERWONE = (40, 28, 28)
TLOZIELONE = (28, 40, 28)
TLONIEBIESKIE = (28, 28, 40)

pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Kolor tła")
clock = pygame.time.Clock()

dziala = True
while dziala:
    clock.tick(FPS)
    
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                dziala = False

    klawisze = pygame.key.get_pressed()
    if klawisze[pygame.K_1]:
        ekran.fill(TLOCZERWONE)
    elif klawisze[pygame.K_2]:
        ekran.fill(TLOZIELONE)
    elif klawisze[pygame.K_3]:
        ekran.fill(TLONIEBIESKIE)

    pygame.display.flip()

