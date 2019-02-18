import pygame

pygame.init()
layar = pygame.display.set_mode((400, 300))
selsai = False
while not selsai:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            selsai = True
    pygame.draw.rect(layar, (0, 255, 128), pygame.Rect(30, 50, 60, 60))
    pygame.draw.rect(layar, (0, 255, 128), pygame.Rect(100, 100, 60, 60)) 
    pygame.display.flip()