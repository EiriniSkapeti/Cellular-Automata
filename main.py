import pygame
import random

# Initialize
pygame.init()

# Constants
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 30
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cellular Automata")
clock = pygame.time.Clock()

# Create first grid
def display_grid():
    return [grid]
     
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


# Main loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen every frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the grid each frame
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = BLACK if grid[y][x] == 1 else WHITE
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)  # Border

    pygame.display.flip()      # << THIS updates the screen
    clock.tick(10)             # Optional: controls how fast the loop runs

pygame.quit()

    
