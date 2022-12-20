# alt: use regex (?<start1>[0-9]+)-(?<end1>[0-9]+),(?<start2>[0-9]+)-(?<end2>[0-9]+)
import re
num_overlap_groups = 0

SPLIT_PATTERN = r",|-"
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        start1, end1, start2, end2 = [int(num) for num in re.split(SPLIT_PATTERN, line)]
        
        if start1 <= start2 <= end1 or start2 <= start1 <= end2:
            num_overlap_groups += 1

print(num_overlap_groups)