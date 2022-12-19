# tuple (x, y, z)
lava_cubes = set()

min_x = min_y = min_z = float('inf')
max_x = max_y = max_z = float('-inf')
# input parsing
with open("input.txt", "r") as f:
    for line in f.readlines():

        cube = line.strip().split(",")
        cube = tuple((int(x) for x in cube))

        lava_cubes.add(cube)
        
        min_x = min(min_x, cube[0])
        min_y = min(min_y, cube[1])
        min_z = min(min_z, cube[2])

        max_x = max(max_x, cube[0])
        max_y = max(max_y, cube[1])
        max_z = max(max_z, cube[2])

# expand bounding box by one so we can consider bubbles against the boundary
min_x -= 1
min_y -= 1
min_z -= 1
max_x += 1
max_y += 1
max_z += 1

def within_bounds(coord):
    return min_x <= coord[0] <= max_x \
        and min_y <= coord[1] <= max_y \
        and min_z <= coord[2] <= max_z

exploration_seed = (min_x, min_y, min_z)
seen_air_bubbles = {exploration_seed}

queue = [exploration_seed]

surface_area = 0

while queue:
    air_cube = queue.pop()

    # print(air_cube)

    for i in range(3):
        for offset in (-1, 1):
            coord = list(air_cube)
            coord[i] += offset
            coord = tuple(coord)
            
            # lava exposed to air from this side
            if coord in lava_cubes:
                surface_area += 1
                continue
            
            # ensure that visited air cubes aren't touched again
            # prevents double-counting surface area
            elif coord in seen_air_bubbles or not within_bounds(coord):
                continue

            seen_air_bubbles.add(coord)
            queue.append(coord)

print(surface_area)