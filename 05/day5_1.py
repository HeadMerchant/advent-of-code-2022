import re
# stacks named 1-9
stacks = [[] for _ in range(9)]

with open("input.txt", "r") as f:
    lines = iter(f.readlines())
    
def parse_stacks():
    for line in lines:
        for i in range(9):
            item = line[1 + 4*i]
            if item.isalpha():
                stacks[i].append(item)
            elif item.isdecimal():
                # skip this line and next blank line
                next(lines)
                return
parse_stacks()

# recover fifo ordering
for stack in stacks:
    stack.reverse()

# parse commands
command_pattern = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")
for command in lines:
    num_move, src_stack, target_stack = (int(num) for num in command_pattern.match(command).groups())
    src_stack -= 1
    target_stack -= 1
    for _ in range(num_move):
        stacks[target_stack].append(stacks[src_stack].pop())

print("".join((stack[-1] for stack in stacks)))