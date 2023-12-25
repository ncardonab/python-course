def find_volume(length = 1, width = 1, depth = 1) -> tuple:
    volume = length * width * depth
    return volume, width, 'This is the volume'

volume, width, string = find_volume(3, 4, 5)

print(string, volume, 'and the width:', width)