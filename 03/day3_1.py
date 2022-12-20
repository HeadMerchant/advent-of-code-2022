PRIORITY_a = ord("a")
PRIORITY_A = ord("A")
def item_priority(char):
    # a-z -> 1-26
    # A-Z -> 27-52
    if char.islower():
        return 1+ord(char)-PRIORITY_a
    
    return 27+ord(char)-PRIORITY_A

# sum of (sum of priorities in intersection of items in compartments for each rucksack)
priority_sum = 0

with open("input.txt", "r") as f:
    for rucksack in f.readlines():
        rucksack = rucksack.strip()
        sack_size = len(rucksack)
        
        compartment_1 = set(rucksack[:sack_size/2])
        compartment_2 = set(rucksack[sack_size/2:])

        priority_sum += sum((item_priority(item) for item in compartment_1 & compartment_2))

print(priority_sum)