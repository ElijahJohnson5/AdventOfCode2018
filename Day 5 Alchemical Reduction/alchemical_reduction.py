input_line = ""

# Read in the lines of input file
# Loop through the lines in the file
for lines in open("input", "r"):
    input_line = lines.strip()


def opposite(a, b):
    return (a.lower() == b.lower()) and ((a.isupper() and b.islower()) or (a.islower() and b.isupper()))


def reaction(line):
    buf = []
    for c in line:
        if buf and opposite(c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
    return len(buf)


agents = set([c.lower() for c in input_line])

print(reaction(input_line))
print(min([reaction(input_line.replace(a, '').replace(a.upper(), ''))
           for a in agents]))
