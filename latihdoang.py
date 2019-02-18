import pygame
from pygame import *
import time

pygame.init()
layar = pygame.display.set_mode((800, 600))
selsai = False
biru = False
while not selsai:
 
 for event in pygame.event.get():
  if event.type == pygame.KEYDOWN:
  if event.type == pygame.QUIT:
   selsai = True

 if not biru:
  warna = (0, 255, 128)
 else:
  warna = (0, 0, 128)

 pygame.draw.rect(layar, warna, pygame.Rect(30, 30, 60, 60))
 pygame.display.flip()
