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

print("-All packages  has been downloaded-")
print("----------Launching  game----------")

import pygame

playerSpaceShip = pygame.image.load("/home/monntheboss/jeu/spaceship.png")

class Player:
    global playerSpaceShip
    def __init__(self):
        self.player = playerSpaceShip
        self.movex = 25

    def display(self):
        screen.fill((0, 0, 0))
        screen.blit(playerSpaceShip, (self.movex, 600))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.movex -= 3
        if keys[pygame.K_RIGHT]:
            self.movex += 3
    def run(self):
        self.display()
        self.move()


x = 1080
y = 720

screen = pygame.display.set_mode((x, y))

pygame.display.set_caption("Galaga")

player = Player()


pygame.init()

running = True
while running:
    player.run()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            


pygame.quit()

