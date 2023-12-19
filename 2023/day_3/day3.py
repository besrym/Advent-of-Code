from typing import Union, Tuple, List


def get_surrounding_chars(x: List, y: int) -> str:
    x1, x2 = x[0] - 1, x[-1] + 2
    y1, y2 = y - 1, y + 2
    surroundings = ""

    x_range = range(max(0, x1), min(len(schematic[0]) - 1, x2))
    y_range = range(max(0, y1), min(len(schematic) - 1, y2))

    for jj in y_range:
        for ii in x_range:
            surroundings += schematic[jj][ii]

    return surroundings


def find_gear(x: List, y: int) -> Union[Tuple, None]:
    x1, x2 = x[0] - 1, x[-1] + 2
    y1, y2 = y - 1, y + 2

    x_range = range(max(0, x1), min(len(schematic[0]) - 1, x2))
    y_range = range(max(0, y1), min(len(schematic) - 1, y2))

    for jj in y_range:
        for ii in x_range:
            if schematic[jj][ii] == "*":
                return jj, ii

    return None


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        schematic = []
        for line in f:
            line = line.replace("\n", "")
            schematic.append(line)

    number_positions = []

    for i, line in enumerate(schematic):
        dig = ""
        for j, char in enumerate(line):
            if char.isdigit():
                dig += char
                if j == len(line) - 1:
                    x_positions = [k for k in range(j - len(dig), j)]
                    number_positions.append((dig, x_positions, i))
                    dig = ""
            elif dig:
                x_positions = [k for k in range(j - len(dig), j)]
                number_positions.append((dig, x_positions, i))
                dig = ""

    sum_part_numbers = 0

    for pos in number_positions:
        valid = False
        surr = get_surrounding_chars(pos[1], pos[2])
        for char in surr:
            if char != "." and not char.isdigit():
                valid = True
        if valid:
            sum_part_numbers += int(pos[0])

    print("result part 1: ", sum_part_numbers)

    gear_ratios = []
    candidates = {}

    for pos in number_positions:
        gear = find_gear(pos[1], pos[2])
        if gear:
            if candidates.get(gear):
                candidates[gear].append(pos[0])
            else:
                candidates[gear] = [pos[0]]

    for gear in candidates:
        if len(candidates[gear]) == 2:
            gear_ratios.append((int(candidates[gear][0]) * int(candidates[gear][1])))

    print("result part 2: ", sum(gear_ratios))
