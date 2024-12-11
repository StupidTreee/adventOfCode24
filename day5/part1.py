
# parse the input
with open('data.txt') as data:
    rules = {}  # Dictionary for the rules in a key:value (hashmap)
    updates = []  # update in a 2d Array 

    for line in data:
        line = line.strip()
        if line == "":
            break
        key, value = line.split('|')  
        rules[key] = int(value) # parse string to int  
    
    print("Rules:", rules)

    for line in data:
        line = line.strip()
        if line: 
            updates.append([int(x) for x in line.split(',')])
    
    for update in updates:
        for rule in rules:
            


    print("Updates (2D-Array):", updates)
