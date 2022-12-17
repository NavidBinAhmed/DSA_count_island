# data structure and algorithm

def islands(input):
    # Keep track of the number of islands
    count = 0

    # Iterate through each cell in the grid
    for i in range(len(input)):
        for j in range(len(input[0])):
            # If the cell is land, perform a depth-first search
            if input[i][j] == 1:
                # verify if the cell meets the condition, then it counts up
                dfs(input, i, j)
                count += 1
    return count


def dfs(input, i, j):
    # Check if the cell is out of bounds or is water
    if i < 0 or i >= len(input) or j < 0 or j >= len(input[0]) or input[i][j] == 0:
        return

    # Mark the cell as water to avoid revisiting it
    input[i][j] = 0

    # Perform a depth-first search on the adjacent cells
    dfs(input, i + 1, j)
    dfs(input, i - 1, j)
    dfs(input, i, j + 1)
    dfs(input, i, j - 1)


# Test the function
sample_input_grid_1 = [[1, 1, 0, 0, 0],
                       [1, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 1]]

sample_input_grid_2 = [[1, 0, 1, 0, 1],
                       [0, 1, 0, 1, 0],
                       [1, 0, 1, 0, 1],
                       [0, 1, 0, 1, 0]]

sample_input_grid_3 = [[1, 0, 1, 0, 1],
                       [0, 1, 0, 1, 0],
                       [1, 0, 1, 0, 1],
                       [0, 1, 0, 1, 0],
                       [1, 0, 1, 1, 0],
                       [1, 1, 0, 1, 1]]

print(islands(sample_input_grid_1))
print(islands(sample_input_grid_2))
print(islands(sample_input_grid_3))
