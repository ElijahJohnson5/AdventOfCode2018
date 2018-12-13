from collections import defaultdict

striped_lines = []
coords = defaultdict(int)
rectangle_set = defaultdict(tuple)


def rect_coords(id_num, offsets, rect_size):
    rect = []
    left_offset, top_offset = [int(x) for x in offsets.split(",")]
    for i in range(0, int(rect_size.split("x")[0])):
        for j in range(0, int(rect_size.split("x")[1])):
            coords[(left_offset + i, top_offset + j)] += 1
            rect.append((left_offset + i, top_offset + j))
    rectangle_set[int(id_num[1:])] = tuple(rect)


# Read in the lines of input file
# Loop through the lines in the file
for line in open("input", "r"):
    line = line.rstrip()
    striped_lines.append(line)
    idNum = line.split(" ")[0]
    distance, size = line.split("@")[1].split(":")
    distance = distance.lstrip()
    size = size.lstrip()
    rect_coords(idNum, distance, size)

count = 0
for key, value in coords.items():
    if value >= 2:
        count += 1
print(count)

for id_num, rect in rectangle_set.items():
    current_id = id_num
    for coord in rect:
        if coords[coord] > 1:
            current_id = 0
            continue
    if current_id != 0:
        print(current_id)

