with open('data.txt') as f:
    data = [line.split(':') for line in f.read().splitlines()]

for i, line in enumerate(data):
    key = int(line[0]) 
    values = list(map(int, line[1].strip().split())) 
    data[i] = [key] + values  


print(data)
