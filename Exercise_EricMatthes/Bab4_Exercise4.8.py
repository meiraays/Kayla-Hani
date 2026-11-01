#membuat list angka pangkat tiga dari 1 sampai 10
cubes = []

for angka in range(1, 11):
    cube = angka ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)