import datetime
from collections import defaultdict
from collections import Counter

sorted_lines = []
time_asleep = defaultdict(int)
guard_times = Counter()
all_guard_times = defaultdict(Counter)


def get_date_from_string(string):
    return datetime.datetime.strptime(string[:18], "[%Y-%m-%d %H:%M]")


# Read in the lines of input file
# Loop through the lines in the file
for line in open("input", "r"):
    line = line.rstrip()
    sorted_lines.append(line)

# Read and sort lines by the date
sorted_lines = sorted(sorted_lines, key=get_date_from_string)
guard_id = -1
start_time = -1
# Part 1 get the current guard id
for line in sorted_lines:
    if "Guard" in line:
        if guard_id != -1:
            if len(guard_times) > 0:
                all_guard_times[guard_id] += guard_times
        guard_id = int(line.split("#")[1].split(" ")[0])
        guard_times = Counter()
    # Get the time the guard falls asleep
    elif "falls asleep" in line:
        start_time = get_date_from_string(line).minute
    # Get the time the guard wakes up
    else:
        end_time = get_date_from_string(line).minute
        # Increment the counter for this guard at the times
        # they were asleep
        for i in range(start_time, end_time):
            guard_times[i] += 1
        # Add to the total time they were asleep
        time_asleep[guard_id] += end_time - start_time
# Get the guard who has the most time asleep
_, guard = max((v, k) for k, v in time_asleep.items())
# Get the time they are asleep the most from the counter
minute_most_asleep = all_guard_times[guard].most_common()[0][0]
# Print answer for part 1
print(guard * minute_most_asleep)

max_occurences = 0
minute = -1
# Loop through all of the guards and the counters for the guards
for key, value in all_guard_times.items():
    # Get the minute that they were asleep the most and the number
    # of days they were asleep on that minute
    minute_most_asleep, occurences = value.most_common()[0]
    # Check if that is greater than the max that we had if so set the guard to the
    # correct guard id and the minute they are asleep on the most
    if occurences > max_occurences:
        max_occurences = occurences
        minute = minute_most_asleep
        guard = key
# Print out part 2 answer
print(guard * minute)
