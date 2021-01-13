hearts = []

for number_card in range(2, 11):
    hearts.append(f"{number_card} of Hearts")
hearts.append("J of Hearts")
hearts.append("Q of Hearts")
hearts.append("K of Hearts")
hearts.append("A of Hearts")

# print all cards in hearts[]
for card in hearts:
    print(card)

# print just number cards
print("\nJust the number cards:")
for card in hearts[:9]:
    print(card)

# print just face cards
print("\nJust the face cards:")
for card in hearts[9:]:
    print(card)
