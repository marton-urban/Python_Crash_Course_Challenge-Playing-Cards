cards = []

# generate all cards in one nested loop
for rank in [*range(2, 11), 'J', 'Q', 'K', 'A']:
    for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
        cards.append(f"{rank} of {suit}")

# print card in just one suit
for card in cards:
    if "Clubs" in card:
        print(card)
