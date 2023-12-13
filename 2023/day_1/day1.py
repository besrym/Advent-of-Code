with open("input.txt", "r") as f:
    result = 0
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in f:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d, val in enumerate(nums):
                if line[i:].startswith(val):
                    digits.append(str(d + 1))
        score = int(f"{digits[0]}{digits[-1]}")
        result += score
    print(result)
