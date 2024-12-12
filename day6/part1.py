map = list(map(list, open('data.txt').read().splitlines()))
for x, line in enumerate(map):
    if '^' in line:
        guard_pos = [x, line.index('^')]
print("guard starts at: ", guard_pos)

direction = [0, 1]

def rotate_90_deg(direction):
    return
print("try +1: " ,guard_pos + direction)

while(guard_pos[0] < len(map) and guard_pos[1] < len(map[0])):
    if map[guard_pos[0] + direction[0], guard_pos[1] + direction[1]] :
        break
        # ka muss noch machen