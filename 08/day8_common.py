with open("input.txt", "r") as f:
    lines = f.readlines()

tree_grid = [[int(height) for height in line.strip()] for line in lines]


width, height = len(tree_grid), len(tree_grid[0])

left_edge = [(row, 0) for row in range(height)]
right_edge = [(row, width-1) for row in range(height)]

top_edge = [(0, col) for col in range(width)]
bottom_edge = [(height-1, col) for col in range(width)]

left_to_right = range(1, width)
right_to_left = range(width-2, -1, -1)
top_to_bottom = range(1, height)
bottom_to_top = range(height-2, -1, -1)