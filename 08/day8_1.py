from day8_common import *

#edge trees are trivially visible
visible_trees = set()
visible_trees.update(left_edge, right_edge, top_edge, bottom_edge)

def sweep_horizontal(edge, col_iter):
    tallest_prev = [tree_grid[r][c] for r, c in edge]
    for c in col_iter:
        for r in range(len(tallest_prev)):
            if (tree_height := tree_grid[r][c]) > tallest_prev[r]:
                visible_trees.add((r, c))
                tallest_prev[r] = tree_height

sweep_horizontal(left_edge, left_to_right)
sweep_horizontal(right_edge, right_to_left)

def sweep_vertical(edge, row_iter):
    tallest_prev = [tree_grid[r][c] for r, c in edge]
    for r in row_iter:
        for c in range(len(tallest_prev)):
            if (tree_height := tree_grid[r][c]) > tallest_prev[c]:
                visible_trees.add((r, c))
                tallest_prev[c] = tree_height

sweep_vertical(top_edge, top_to_bottom)
sweep_vertical(bottom_edge, bottom_to_top)


print(len(visible_trees))