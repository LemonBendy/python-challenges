#create game of life

import pygame
import random
import time

pygame.init()

#set up the window
width = 1000
height = 1000
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
fps = 0
clock = pygame.time.Clock()

#set up the font
font = pygame.font.SysFont("Arial", 16)

#set up the grid
def setup_grid():
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = random.randint(0, 1)

#draw the grid
def draw_grid():
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, white, (j * cell_size, i * cell_size, cell_size, cell_size), 0)
            else:
                pygame.draw.rect(screen, black, (j * cell_size, i * cell_size, cell_size, cell_size), 0)

#update the grid
def update_grid():
    global generation
    for i in range(rows):
        for j in range(cols):
            neighbors = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if i + x < 0 or i + x >= rows or j + y < 0 or j + y >= cols:
                        continue
                    if grid[i + x][j + y] == 1:
                        neighbors += 1
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    next_grid[i][j] = 0
                else:
                    next_grid[i][j] = 1
            else:
                if neighbors == 3:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0
    grid[:] = next_grid[:]
    generation += 1


#clear grid
def clear_grid():
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = 0


def config_1():
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = 0
    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1

def config_2():
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = 0
    for u in range(rows):
            grid[u][25] = 1
            grid[u][26] = 1

def config_3():
    #gosper's glider gun
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = 0
    grid[5][1] = 1
    grid[5][2] = 1
    grid[6][1] = 1
    grid[6][2] = 1
    grid[5][11] = 1
    grid[6][11] = 1
    grid[7][11] = 1
    grid[4][12] = 1
    grid[3][13] = 1
    grid[3][14] = 1
    grid[8][12] = 1
    grid[9][13] = 1
    grid[9][14] = 1
    grid[6][15] = 1
    grid[4][16] = 1
    grid[5][17] = 1
    grid[6][17] = 1
    grid[7][17] = 1
    grid[6][18] = 1
    grid[8][16] = 1
    grid[3][21] = 1
    grid[4][21] = 1
    grid[5][21] = 1
    grid[3][22] = 1
    grid[4][22] = 1
    grid[5][22] = 1
    grid[2][23] = 1
    grid[6][23] = 1
    grid[1][25] = 1
    grid[2][25] = 1
    grid[6][25] = 1
    grid[7][25] = 1
    grid[3][35] = 1
    grid[3][36] = 1
    grid[4][35] = 1
    grid[4][36] = 1

def config_4():
    #gilbert's glider gun
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = 0
    grid[5][1] = 1
    grid[5][2] = 1
    grid[6][1] = 1
    grid[6][2] = 1
    grid[5][11] = 1
    grid[6][11] = 1
    grid[7][11] = 1
    grid[4][12] = 1
    grid[3][13] = 1
    grid[3][14] = 1
    grid[8][12] = 1
    grid[9][13] = 1
    grid[9][14] = 1
    grid[6][15] = 1
    grid[4][16] = 1
    grid[5][17] = 1
    grid[6][17] = 1
    grid[7][17] = 1
    grid[6][18] = 1
    grid[8][16] = 1
    grid[3][21] = 1
    grid[4][21] = 1
    grid[5][21] = 1
    grid[3][22] = 1
    grid[4][22] = 1
    grid[5][22] = 1
    grid[2][23] = 1
    grid[6][23] = 1
    grid[1][25] = 1
    grid[2][25] = 1
    grid[6][25] = 1
    grid[7][25] = 1
    grid[3][35] = 1
    grid[3][36] = 1
    grid[4][35] = 1
    grid[4][36] = 1
    grid[2][13] = 1
    grid[2][14] = 1
    grid[7][13] = 1
    grid[7][14] = 1


#main loop
def main():
    global running
    global paused
    global generation
    global start_time
    global fps

#run the game loop
setup_grid()
while running:
    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            if event.key == pygame.K_r:
                setup_grid()
                generation = 0
                start_time = time.time()
                fps = 0
            if event.key == pygame.K_c:
                clear_grid()
                generation = 0
                start_time = time.time()
                fps = 0
            if event.key == pygame.K_s:
                pygame.image.save(screen, "Game of Life.png")
            if event.key == pygame.K_1:
                config_1()
                generation = 0
                start_time = time.time()
                fps = 0
            if event.key == pygame.K_2:
                config_2()
                generation = 0
                start_time = time.time()
                fps = 0
            if event.key == pygame.K_3:
                config_3()
                generation = 0
                start_time = time.time()
                fps = 0

    #update the screen
    screen.fill(black)
    draw_grid()
    if not paused:
        update_grid()
    text = font.render("Generation: " + str(generation), True, red)
    screen.blit(text, (10, 10))
    text = font.render("FPS: " + str(round(fps,0)), True, red)
    screen.blit(text, (10, 30))
    pygame.display.flip()
    clock.tick(30)
    fps = clock.get_fps()

if __name__ == "__main__":
    main()

