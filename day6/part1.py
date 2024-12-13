map = list(map(list, open('data.txt').read().splitlines()))
for x, line in enumerate(map):
    if '^' in line:
        guard_pos = [x, line.index('^')]


for line in map:
    print(line)
print("guard starts at: ", guard_pos)

direction = [-1, 0]

def rotate_90_deg(direction):
    return [direction[1], -direction[0]]

while(0 <= guard_pos[0] < len(map) and 0 <= guard_pos[1] < len(map[0])):
    try:
        if map[guard_pos[0] + direction[0]] [guard_pos[1] + direction[1]] == '#' :
            direction = rotate_90_deg(direction)
    except:
        break
    map[guard_pos[0]][guard_pos[1]] = 'X'
    
    guard_pos[0] += direction[0]
    guard_pos[1] += direction[1]
    map[guard_pos[0]][guard_pos[1]] = '^'
    print(guard_pos)
for line in map:
    print(line)
print("guard has left the map at:", guard_pos, "and in direction: ", direction)
total = 1
for line in map:
    for tile in line:
        if tile == 'X':
            total += 1
print("guard walked ", total, " tiles")