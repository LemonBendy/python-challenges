#game of life

import pygame
import random
import time

#set up the screen
pygame.init()
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game of Life")

#set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#set up the variables
cell_size = 10
cols = width // cell_size
rows = height // cell_size
grid = [[0 for x in range(cols)] for y in range(rows)]
next_grid = [[0 for x in range(cols)] for y in range(rows)]
running = True
paused = False
generation = 0
start_time = time.time()

