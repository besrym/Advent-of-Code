with open("input.txt", "r") as f:
    end_score = 0
    cards = []
    for line in f:
        line = line.split()
        card_id = line[1].replace(":", "")
        winning_numbers = line[2:12]
        my_numbers = line[13:]

        matches = sum(elem in my_numbers for elem in winning_numbers)

        cards.append([card_id, winning_numbers, my_numbers, matches, False, 1])

        score = 0
        if matches > 1:
            score = 2 ** (matches - 1)
        if matches == 1:
            score = 1
        end_score += score

    print("part 1: ", end_score)

    for card in cards:

        id = int(card[0])
        wins = int(card[3])

        for _ in range(card[5]):
            for j in range(id + 1, id + wins + 1):
                cards[j - 1][5] += 1

    result = 0
    for card in cards:
        result += card[5]
    print("part 2: ", result)
