
def sort_cards(cards):
    sorted_cards = sorted(cards, key=lambda card: card_strenghts[card])
    return ''.join(sorted_cards)


def detect_hand(hand):
    pass


def sort_strength(hands):
    pass


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        camel_cards = []
        for line in file:
            camel_cards.append(line.split())

    card_strenghts = {"A": 12,
                      "K": 11,
                      "Q": 10,
                      "J": 9,
                      "T": 8,
                      "9": 7,
                      "8": 6,
                      "7": 5,
                      "6": 4,
                      "5": 3,
                      "4": 2,
                      "3": 1,
                      "2": 0}


