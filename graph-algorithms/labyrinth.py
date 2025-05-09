#✅ Improved Version with Comments and Bounds Checking:
def explore(grid, y, x):
    # Check if coordinates are out of bounds
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return
    
    # Only explore cells that are 0 (unvisited)
    if grid[y][x] != 0:
        return

    print("visit", y, x)
    grid[y][x] = 2  # Mark as visited

    # Explore 4-connected neighbors (up, down, left, right)
    explore(grid, y - 1, x)  # Up
    explore(grid, y + 1, x)  # Down
    explore(grid, y, x - 1)  # Left
    explore(grid, y, x + 1)  # Right

# Grid: 1 = wall, 0 = open, 2 = visited
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

explore(grid, 1, 1)  # Start exploration from position (1, 1)

# Print final grid
for row in grid:
    print(row)

# 🧠 Output Explanation
# After running explore(grid, 1, 1), it will:

# Visit all 0s that are connected to position (1, 1) by 4-way movement (no diagonals).

# Convert them to 2 to mark them as visited.

# Ignore 1s (walls) and stay within the bounds of the grid.

