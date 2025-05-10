def count_neighbors(grid, x, y, width, height):
    neighbors = 0
    for dy in [-1, 0, 1]:
        for dx in[-1, 0, 1]:
           nx, ny = x + dx, y + dy
           if dx == 0 and dy == 0:
               continue
           if 0<= nx < width and 0<= ny < height:
               neighbors += grid[ny][nx]
               
    return neighbors 
       
def update_grid(grid,width,height):
    new_grid= [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            neighbors = count_neighbors(grid, x, y, width, height)
            if grid[y][x] == 1 :
                if neighbors == 2 or neighbors == 3:
                    new_grid[y][x] = 1 #survives
                else:
                        new_grid[y][x] = 0 #dies
            else:
                if neighbors == 3:
                    new_grid[y][x] = 1
    return new_grid