import os
import random
import asyncio
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
