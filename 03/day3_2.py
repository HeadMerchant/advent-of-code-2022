PRIORITY_a = ord("a")
PRIORITY_A = ord("A")
def item_priority(char):
    # a-z -> 1-26
    # A-Z -> 27-52
    if char.islower():
        return 1+ord(char)-PRIORITY_a
    
    return 27+ord(char)-PRIORITY_A

priority_sum = 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        elf_group = (set(line.strip()) for line in lines[i:i+3])
        common_items = set.intersection(*elf_group)

        # only one item in set
        badge_priority  = item_priority(common_items.pop())
        priority_sum += badge_priority

print(priority_sum)