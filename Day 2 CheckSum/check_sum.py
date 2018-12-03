import collections

two_char = set()
three_char = set()
striped_lines = []
# Read in the lines of input file
# Loop through the lines in the file
for line in open("input", "r"):
    line = line.rstrip()
    striped_lines.append(line)
    d = collections.defaultdict(int)
    # Keep dictionary with count of times seen letter
    for c in line:
        d[c] += 1

    # Loop through dictionary and check if there are
    # Exactly 2 or 3 of those letters in the string then
    # Add the string to a set
    for key, value in d.items():
        if value == 2 and line not in two_char:
            two_char.add(line)

        if value == 3 and line not in three_char:
            three_char.add(line)


print(len(two_char)*len(three_char))

for first in striped_lines:
    for second in striped_lines:
        diff = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                diff += 1
        if diff == 1:
            ans = []
            for i in range(len(first)):
                if first[i] == second[i]:
                    ans.append(first[i])

            print(''.join(ans))
