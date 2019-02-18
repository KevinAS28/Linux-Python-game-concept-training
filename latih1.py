#!/usr/bin/python3

import pygame
import os
import sys
import time

pygame.init()
screen = pygame.display.set_mode((1000,  800))
done = False

while not done:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   done = True

 pygame.display.flip()
