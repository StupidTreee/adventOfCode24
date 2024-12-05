import numpy as np
from itertools import product

with open("data.txt", "r") as data:
    lines = data.readlines()

linesCount = len(lines)
charCount = len(lines[0])
matrix = [[char for char in line.strip()] for line in lines]

for line in matrix:
    print(line)