# tuple (x, y, z)
cubes = set()

# input parsing
with open("input.txt", "r") as f:
    for line in f.readlines():

        cube = line.strip().split(",")
        cube = tuple((int(x) for x in cube))

        cubes.add(cube)

surface_area = 0
# check if neighboring cubes in each direction

for cube in cubes:
    for i in range(3):
        for offset in (-1, 1):
            coord = list(cube)
            coord[i] += offset
            if tuple(coord) not in cubes:
                surface_area += 1

print(surface_area)
