import functools
# parse the input
with open('data.txt') as data:
    rules = []  # rules in a 2d Array
    updates = []  # update in a 2d Array
    correct_order = [] # updates in correct order
    incorrect_order = [] # updates in incorrect order

    for line in data:
        line = line.strip()
        if line == "":
            break  
        rules.append(line.split('|'))
    
    print("Rules:", rules)

    for line in data:
        line = line.strip()
        if line: 
            updates.append(line.split(','))

print("Updates (2D-Array):", updates)

for update in updates:
    for rule in rules:
        if rule[0] in update and rule[1] in update:  # Check if elements exist
            rul0 = update.index(rule[0])
            rul1 = update.index(rule[1])
            if rul1 < rul0:
                incorrect_order.append(update)
                break
    else:
        correct_order.append(update)


def compare(x, y):
    # Iterate over rules
    for rule in rules:
        if rule[0] == x and rule[1] == y:
            return -1  # x should come before y
        if rule[0] == y and rule[1] == x:
            return 1  # y should come before x
    return 0  # No specific order


for update in incorrect_order:
    update.sort(key=functools.cmp_to_key(compare)) 

        

num = [] # array for middle numbers
for list in incorrect_order:
    num.append(int(list[len(list)//2])) # get element and parse to int

print("sum of middle number in incorrect lists: ", sum(num))
