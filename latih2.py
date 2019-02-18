#!/usr/bin/python3

import pygame
import random
import time
from pygame.locals import *



pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))


player = pygame.image.load("player1.gif")    
biru = True
x = 500
y = 30
clock = pygame.time.Clock()
while 1:

    

    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0) 
#        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#         biru = not biru

    pressed = pygame.key.get_pressed()
#    if pressed[pygame.K_UP]: y -= 3
#    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if x <= 30: x = 30
    if x >= 500: x = 500
  

#    screen.fill(0)
#    screen.blit(player, (200, 200))
#    pygame.display.flip()
#    screen.fill(0)
    screen.fill((0, 0, 0))
    if biru:
     color = (0, 128, 255)
    else:
     color = (255, 100, 0)
    screen.blit(player, (x, 300))
#    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(120)




oke = """
pygame.init()
lebar, panjang = 1280, 720
layar = pygame.dislpay.set_mode((lebar, panjang))

pemain = pygame.image.load('player1.gif')

while 1:
 layar.fill(0)
 layar.blit(pemain, (100, 100))
 pygame.display.flip()
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   exit(0)
"""
