import os
import random

try:
	import pygame
	import asyncio
except ImportError:
	print("___Downloading and verifying packages___")
	yn = input("___Do you want to download them [Y/n]___")
	if yn.lower() == "y":
		os.system("pip install pygame")
		os.system("pip install asyncio")
	else:
		print("Abort quitting the programm")
