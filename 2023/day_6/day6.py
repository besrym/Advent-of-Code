import time

# Input
time_p1 = [44, 80, 65, 72]
distance = [208, 1581, 1050, 1102]

# Solution Part 1
record_broken = []

for t, d in zip(time_p1, distance):
    broken_t = []
    for acc in range(1, t):
        remaining_time = t - acc
        traveled_distance = remaining_time * acc
        if traveled_distance > d:
            broken_t.append(acc)
    record_broken.append(len(broken_t))

result = 1

for e in record_broken:
    result *= e

print("part 1: ", result)

# Solution Part 2.1
result = 0
t_0 = time.time()
for acc in range(1, 44806572):
    remaining_time = 44806572 - acc
    traveled_distance = remaining_time * acc
    if traveled_distance > 208158110501102:
        result += 1
t_1 = time.time()

print("part 2.1: ", result, " in ", t_1 - t_0, "s")

# Solution Part 2.2
t_0 = time.time()
time_p2 = 44806572
distance_p2 = 208158110501102
times = list(range(1, time_p2))
result_list = map(lambda x: (time_p2 - x) * x, times)
result_list = filter(lambda x: x > distance_p2, result_list)
result = len(list(result_list))
t_1 = time.time()
print("part 2.2: ", result, " in ", t_1 - t_0, "s")
