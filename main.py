import pygame
import random

# Initialize
pygame.init()

# Constants
CELL_SIZE = 10
GRID_WIDTH = 150
GRID_HEIGHT = 70
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

#from rules.conway import update_grid
from rules.rule30 import update_grid as rule30
from rules.rule90 import update_grid as rule90
from rules.rule182 import update_grid as rule182 
from rules.rule126 import update_grid as rule126
from rules.rule150 import update_grid as rule150

rule_set = {
    "Rule 30": rule30,
    "Rule 90": rule90,
    "Rule 182": rule182,
    "Rule 126": rule126,
    "Rule 150": rule150,
}

# Main loop

simulate = False
running = True

while running:
    screen.fill(WHITE)  # Clear the screen every frame
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.K_SPACE:
            if event.key == pygame.K_SPACE:
                simulate = not simulate
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulate = True

                mid_x = GRID_WIDTH // 2
                grid[0][mid_x]= 1 

            selected_name, update_grid = random.choice(list(rule_set.items()))
            print(f"Using {selected_name}")

    if simulate:
        grid = update_grid(grid, GRID_WIDTH, GRID_HEIGHT)

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

    
