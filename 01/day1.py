current_calories = 0
calories = []
with open("day1.txt", "r") as f:
    for line in f.readlines():
        if line == "\n":
            calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
    calories.append(current_calories)
print(max(calories))

# part 2
calories.sort()
print(sum(calories[-3::]))