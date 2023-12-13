# PART 1

with open("input.txt", "r") as f:
    result = 0
    for line in f:
        sep = line.split(":")
        game_id = sep[0].split(" ")[1]
        hints = sep[1].split(";")
        red, green, blue = True, True, True
        for hint in hints:
            hint = hint.split(",")
            for b in hint:
                b = b.strip()
                b = b.split(" ")
                count = int(b[0])
                color = b[1]
                if color == "red" and count > 12:
                    red = False
                if color == "green" and count > 13:
                    green = False
                if color == "blue" and count > 14:
                    blue = False
        if red and green and blue:
            result += int(game_id)
    print("part 1: ", result)

# PART 2

with open("input.txt", "r") as f:
    result = 0
    for line in f:
        sep = line.split(":")
        game_id = sep[0].split(" ")[1]
        hints = sep[1].split(";")
        red, green, blue = 0, 0, 0
        for hint in hints:
            hint = hint.split(",")
            for b in hint:
                b = b.strip()
                b = b.split(" ")
                count = int(b[0])
                color = b[1]
                if color == "red" and count > red:
                    red = count
                if color == "green" and count > green:
                    green = count
                if color == "blue" and count > blue:
                    blue = count
        tmp = 1
        for c in [red, green, blue]:
            if c != 0:
                tmp *= c
        result += tmp
    print("part 2: ", result)
