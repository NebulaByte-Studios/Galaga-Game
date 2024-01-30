import os
import random
import asyncio

# Vérif des packages
print("-----------------------------------")
print("--------Verifying  packages--------")
try:
	import pygame
except ImportError:
	print("---Downloading  missing packages---")        
	yn = input("---Do you want to download [Y/n]---")
	if yn.lower() == "y":
		os.system("pip install pygame")
	else:
		print("Abort quitting the programm")
		exit()

import pygame

# Création de la fenêtre
x = 1080
y = 720

screen = pygame.display.set_mode((x, y))

pygame.display.set_caption("Galaga")


pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
