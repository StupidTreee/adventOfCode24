from itertools import product

with open("data.txt", "r") as data:
    lines = data.readlines()

linesCount = len(lines)
charCount = len(lines[0])
matrix = [[char for char in line.strip()] for line in lines]

for line in matrix:         
    print(line)

def valid_indexes(matrix, row, col):
    """Check if the given row and column are within bounds."""
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

def find_word(matrix, word, row, col, dr, dc):
    """Check if a word exists starting at (row, col) in the direction (dr, dc)."""
    for i in range(len(word)-2):
        r, c = row + dr * i, col + dc * i
        if not valid_indexes(matrix, r, c) or matrix[r][c] != word[1]:
            return False
    return True

def find_X_MAS(matrix, word, row, col, directions):
    # Check if a word exists in a X Shape starting at (row, col) 
    for dir in directions:
        for i in range(len(word)):
            r, c = row + dir[0] * (-i), col + dir[1] * (-i)
            if not valid_indexes(matrix, dir[0], dir[1]) or matrix[r][c] != word[i]:
                return False
        return True

def find_all_occurrences(matrix, word):
    """Find all occurrences of a word in the matrix."""
    directions = list(product([-1, 1], repeat=2)) 
    #directions.remove((0, 0))
    found_positions = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for dr, dc in directions:
                if (matrix[i][j] == 'A'):
                    if find_X_MAS(matrix, word, i, j, directions):
                        found_positions.append((i, j, dr, dc))

    return found_positions

word_to_find = "MAS"
positions = find_all_occurrences(matrix, word_to_find)

print(f"Found {word_to_find} at the following positions and directions:")
for position in positions:
    start_row, start_col, dr, dc = position
    print(f"Start: ({start_row}, {start_col}), Direction: ({dr}, {dc})")


print("Amount of 'X-MAS' found is ", len(positions))
