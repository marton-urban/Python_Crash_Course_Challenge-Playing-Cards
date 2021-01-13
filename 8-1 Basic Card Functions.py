def build_deck():
    """Returns a list of all the cards in a standard deck, in order."""
    full_deck = []
    for rank in [*range(2, 11), 'J', 'Q', 'K', 'A']:
        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            full_deck.append(f"{rank} of {suit}")

    return full_deck


def get_suit(card):
    """Returns the suit of one card"""
    return card.split()[-1]


def get_value(card):
    """Returns the value of one card"""
    return card.split()[0]


def same_value(*cards):
    """Returns True if 2 cards have the same value, otherwise returns False"""
    counter = 1
    for card in cards[:-1]:
        for card2 in cards[counter:]:
            if get_value(card) != get_value(card2):
                return False
        counter += counter

    return True


def same_suit(*cards):
    """Returns True if all cards have the same suit, otherwise returns False"""
    counter = 1
    for card in cards[:-1]:
        for card2 in cards[counter:]:
            if get_suit(card) != get_suit(card2):
                return False
        counter += counter

    return True


print(same_value('1 of Diamonds', '2 of Diamonds', '3 of Diamonds'))
print(same_suit('1 of Diamonds', '2 of Diamonds', '3 of Diamonds'))
print(same_value('1 of Diamonds', '1 of Diamonds', '1 of Diamonds'))