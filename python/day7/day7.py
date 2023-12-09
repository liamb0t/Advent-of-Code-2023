def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day7/data.txt'
data = read_data_from_file(file_path)

letter_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}

games = [(line.split()[0], int(line.split()[1])) for line in data]

def hand_type(hand):
    card_counts = [hand.count(card) for card in hand]
    if 5 in card_counts:
        return 6
    if 4 in card_counts:
        return 5
    if 3 in card_counts:
        return 4 if 2 in card_counts else 3
    if card_counts.count(2) == 4:
        return 2
    if card_counts.count(2) == 2 and card_counts.count(1) == 3:
        return 1
    return 0

def new_hand(hand):
    card_counts = [(hand.count(card), card) for card in hand if card != 'J']
    rankings = sorted(card_counts)
    if len(rankings) > 0:
        strongest = rankings[-1][1]
        return [strongest if card == 'J' else card for card in hand]
    else:
        return 'AAAAA'

def hand_rank(hand):
    strongest_hand = None
    if 'J' in hand:
        strongest_hand = new_hand(hand)
    return (hand_type(strongest_hand if strongest_hand else hand), [letter_map.get(card, card) for card in hand])
    
rankings = sorted(games, key=lambda hand: hand_rank(hand[0]))

winnings = 0

for rank, game in enumerate(rankings, 1):
    bid = game[1]
    winnings += bid * rank

print(winnings)
