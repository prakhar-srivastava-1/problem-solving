def is_visible(m, n, grid):
    # m = row
    # n = col
    columns = len(grid[0])
    rows = len(grid)
    
    col_list = []
    row_list = []

    # check horizontally
    for j in range(0, columns):
        row_list.append(grid[m][j])
    
    left = max(row_list[:n])
    right = max(row_list[n+1:])
       
    # check vertically
    for j in range(0, rows):
        col_list.append(grid[j][n])

    up = max(col_list[:m])
    down = max(col_list[m+1:])
       
    current_elem = grid[m][n]

    # check if the tree is tallest from any of the directions
    if current_elem > up or current_elem > down or current_elem > left or current_elem > right:
        return True
    return False 

# for debugging
def print_grid(grid):
    for each_row in grid:
        print(each_row)

# read the input file
with open("input.txt", "r") as input_file:
    data = input_file.read()
    data = data.split("\n")

grid = []
for each_line in data:
    grid.append(list(map(int, list(each_line))))

columns = len(grid[0])
rows = len(grid)

# since its a square matrix
# should be changed if generic
# get edge_trees (perimeter)
edge_trees = 2 * (columns + columns - 2)

start_index = 1
end_index = columns - 1

ctr = 0

# drive the loop for inner square
for i in range(start_index, end_index):
    for j in range(start_index, end_index):
        if is_visible(i, j, grid):
            ctr += 1

print(edge_trees + ctr)

# PART TWO

def count_visible(m, n, grid):
    # m = row
    # n = col
    columns = len(grid[0])
    rows = len(grid)
    
    col_list = []
    row_list = []
    left_count, right_count, up_count, down_count = 0, 0, 0, 0

    # check horizontally
    for j in range(0, columns):
        row_list.append(grid[m][j])
    
    left = row_list[:n]
    right = row_list[n+1:]
    # reverse the left 
    left[:] = left[::-1]
       
    # check vertically
    for j in range(0, rows):
        col_list.append(grid[j][n])

    up = col_list[:m]
    down = col_list[m+1:]
    # reverse the up list
    up[:] = up[::-1]
    
    current_elem = grid[m][n]

    # traverse left
    for item in left:
        if item < current_elem:
            left_count += 1
        else:
            left_count += 1
            break

    # traverse right
    for item in right:
        if item < current_elem:
            right_count += 1
        else:
            right_count += 1
            break

    # traverse up
    for item in up:
        if item < current_elem:
            up_count += 1
        else:
            up_count += 1
            break

    # traverse down
    for item in down:
        if item < current_elem:
            down_count += 1
        else:
            down_count += 1
            break
    
    # calculate and return score
    return left_count * right_count * down_count * up_count

# sentinel    
max_score = -99999

# drive the loop for inner square and get max_score
for i in range(start_index, end_index):
    for j in range(start_index, end_index):
        this_score = count_visible(i, j, grid)
        if this_score > max_score:
            max_score = this_score

print(max_score)
            