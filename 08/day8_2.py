from day8_common import *

visibility_scores = [[1]*height for _ in range(width)]

# monotonic stack of next greatest element
def sweep_horizontal(edge, col_iter):
    tallest_prev = [[(tree_grid[r][c], c)] for r, c in edge]
    _, start_col = tallest_prev[0][0]
    for c in col_iter:
        for r, row_stack in enumerate(tallest_prev):
            current_height = tree_grid[r][c]

            while row_stack:
                prev_height, prev_c = row_stack[-1]
                if current_height >= prev_height:
                    row_stack.pop()
                
                # stop on trees of same height, but current height will be spatially closer to future queries
                if current_height <= prev_height:
                    visibility_scores[r][c] *= abs(prev_c-c)
                    break
            else:
                visibility_scores[r][c] *= abs(c - start_col)
            
            row_stack.append((current_height, c))


sweep_horizontal(left_edge, left_to_right)
sweep_horizontal(right_edge, right_to_left)

# monotonic stack of next greatest element
def sweep_vertical(edge, row_iter):
    tallest_prev = [[(tree_grid[r][c], r)] for r, c in edge]
    _, start_row = tallest_prev[0][0]
    for r in row_iter:
        for c, col_stack in enumerate(tallest_prev):
            current_height = tree_grid[r][c]

            while col_stack:
                prev_height, prev_r = col_stack[-1]
                if current_height >= prev_height:
                    col_stack.pop()
                
                # stop on trees of same height, but current height will be spatially closer to future queries
                if current_height <= prev_height:
                    visibility_scores[r][c] *= abs(prev_r-r)
                    break
            else:
                visibility_scores[r][c] *= abs(r - start_row)
            
            col_stack.append((current_height, r))


sweep_vertical(top_edge, top_to_bottom)
sweep_vertical(bottom_edge, bottom_to_top)

print(
    max((
        max(row) for row in visibility_scores
    ))
)