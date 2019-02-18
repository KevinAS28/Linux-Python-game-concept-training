#!/usr/bin/python

import time
import pygame
import os
import sys
from time import sleep as sl
from threading import Thread
import daemon
from Crypto.Cipher import AES
import platform
#from spam import do_main_program
#from pygame import *

pygame.init()
layar = pygame.display.set_mode((1024, 720))
xx = 300
yy = 0
selsai = False
cepat = 60
posisi = [1, 2, 3]
letak = 30
batas1, batas2 = -50, 600
score = 0
warna = (255, 100, 0)
finish = []
for cba in range(550, 600):
 finish.append(cba)
clock = pygame.time.Clock()
skarang = time.ctime()
xx1 = 600
yy1 = 0
jam = pygame.time.Clock()

#def kotak1(x, y, warna):
 
#def cek():
 
print(os.getcwd())
os.chdir('/root/Music')
print(os.getcwd())
time.sleep(0.5)
#try: os.system('killall vlc') #memastikan ga ada vlc
#except: pass



def mantap():
 with daemon.DaemonContext():
  try:
   os.system('killall vlc')
  except:
   pass
  os.system('vlc n.mp3')

okeko = Thread(target=mantap, args=[])
#okeko.start()
"""
def laguu():
 try: os.system('killall vlc') #memastikan ga ada vlc
 except: os.system(' ')
 os.system('cvlc n.mp3') #daemon	
"""

#global yy

def speed(x):
 global yy 
 for kevin in range(x):

  yy += 1
#  return yy


def speed1(x):
 global yy1
 for nivek in range(x):
  yy1 += 1
#gambar kotak bergerak

def kotak():
# time.sleep(2)
 while True:
  pygame.draw.rect(layar, warna, pygame.Rect(xx, yy, 60, 60)) 

print(os.getcwd())
os.chdir('/root/programming/python_saya/pygame')
pemain = pygame.image.load("player1.gif")    

while not selsai:
 for kevin in pygame.event.get():
  if kevin.type == pygame.QUIT:
   selsai = True

  terpencet = pygame.key.get_pressed()
  if terpencet[pygame.K_UP] and (yy in finish):
   score += 10
   os.system("zenity --error --text='oke' --title='wow' ")
   sys.exit()


  if terpencet[pygame.K_UP] and (yy1 in finish):
   score += 10
   os.system("zenity --error --text='oke' --title='wow' ")
   sys.exit()


 layar.fill((0, 0, 0))

# if yy >= 720:
#  yy = 0
#  y1 = 0
 pygame.draw.rect(layar, warna, pygame.Rect(600, yy1, 60, 60))
  

 pygame.draw.rect(layar, warna, pygame.Rect(xx, yy, 60, 60))
# pygame.draw.rect(layar, warna, pygame.Rect(600, y, 60, 60))
 pygame.draw.rect(layar, (255, 0, 0), pygame.Rect(batas1, batas2, 1400, 10))
# layar.blit(pemain, (xx1, yy1))
# if y == 500:
#  os.system('zenity --error')#  y = 0
# pygame.draw.rect(layar, warna, pygame.Rect(x, y, 60, 60))
# if True :
#  layar.fill((0, 0, 0))

# if (int(y)) == (int(500)): os.system("zenity --error --text='oke' --title='wow'")#  y = 0

#  pygame.draw.rect(layar, warna, pygame.Rect(x, y, 60, 60))

 if yy <= 720:
  speed(5)
#  speed1(5)
 if yy >= 720:
  speed1(5)

# y += 1
# y += 1
# y += 1
# y += 1
# y += 1
# y += 1

# y1 += 1
# y1 += 1
# y1 += 1
	
 os.system('')




# layar.fill((0, 0, 0)) 
 pygame.display.flip()
 clock.tick(60)






