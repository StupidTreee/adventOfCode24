import numpy as np
from itertools import product

with open("data.txt", "r") as data:
    lines = data.readlines()

linesCount = len(lines)
charCount = len(lines[0])
matrix = [[char for char in line.strip()] for line in lines]

for line in matrix:
    print(line)

def valid_indexes(lst, row, col):
    """Check if the given row and column are within bounds."""
    return 0 <= row < len(lst) and 0 <= col < len(lst[0])

def find_word(lst, word, row, col, dr, dc):
    """Check if a word exists starting at (row, col) in the direction (dr, dc)."""
    for i in range(len(word)):
        r, c = row + dr * i, col + dc * i
        if not valid_indexes(lst, r, c) or lst[r][c] != word[i]:
            return False
    return True

def find_all_occurrences(lst, word):
    """Find all occurrences of a word in the matrix."""
    directions = list(product([-1, 0, 1], repeat=2)) 
    directions.remove((0, 0))
    found_positions = []

    for i in range(len(lst)):
        for j in range(len(lst[0])):
            for dr, dc in directions:
                if find_word(lst, word, i, j, dr, dc):
                    found_positions.append((i, j, dr, dc))

    return found_positions

word_to_find = "XMAS"
positions = find_all_occurrences(matrix, word_to_find)

print(f"Found {word_to_find} at the following positions and directions:")
for position in positions:
    start_row, start_col, dr, dc = position
    print(f"Start: ({start_row}, {start_col}), Direction: ({dr}, {dc})")


print("amount of 'XMAS' found is ", len(positions))
