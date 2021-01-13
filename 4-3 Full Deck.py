cards = []
ranks = []
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

# generate all ranks
for number_card in range(2, 11):
    ranks.append(number_card)
ranks.append('J')
ranks.append('Q')
ranks.append('K')
ranks.append('A')

# generate all cards
for rank in ranks:
    for suit in suits:
        cards.append(f"{rank} of {suit}")

# print card in just one suit
for rank in ranks:
    print(f"{rank} of Hearts")
