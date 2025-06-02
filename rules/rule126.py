#rule126

def update_grid(grid, width, height):
    new_grid = [[0 for _ in range(width)]for _ in range(height)]
    new_grid[0] = grid[0][:]

    for y in range(height-1):
        for x in range (1, width-1):
            if grid[y][x] == 0 and grid[y][x-1]== 0 and grid[y][x+1]== 0: new_grid[y+1][x]= 0
            elif grid[y][x] == 0 and grid[y][x-1]== 0 and grid[y][x+1]== 1: new_grid[y+1][x]= 1
            elif grid[y][x] == 1 and grid[y][x-1]== 0 and grid[y][x+1]== 0: new_grid[y+1][x]= 1
            elif grid[y][x] == 1 and grid[y][x-1]== 0 and grid[y][x+1]== 1: new_grid[y+1][x]= 1
            elif grid[y][x] == 0 and grid[y][x-1]== 1 and grid[y][x+1]== 0: new_grid[y+1][x]= 1
            elif grid[y][x] == 0 and grid[y][x-1]== 1 and grid[y][x+1]== 1: new_grid[y+1][x]= 1
            elif grid[y][x] == 1 and grid[y][x-1]== 1 and grid[y][x+1]== 0: new_grid[y+1][x]= 1
            elif grid[y][x] == 1 and grid[y][x-1]== 1 and grid[y][x+1]== 1: new_grid[y+1][x]= 0

    
    return new_grid