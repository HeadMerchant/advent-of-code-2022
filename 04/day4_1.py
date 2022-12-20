# alt: use regex (?<start1>[0-9]+)-(?<end1>[0-9]+),(?<start2>[0-9]+)-(?<end2>[0-9]+)
import re
num_subset_groups = 0

SPLIT_PATTERN = r",|-"
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        start1, end1, start2, end2 = [int(num) for num in re.split(SPLIT_PATTERN, line)]
        
        one_contains_two = start1 <= start2 and end2 <= end1
        two_contains_one = start2 <= start1 and end1 <= end2
        if one_contains_two or two_contains_one:
            num_subset_groups += 1

print(num_subset_groups)