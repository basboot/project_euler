import math
from functools import cache

N = 5
n_cards = 2*N

cards = list(range(N)) * 2

print(cards)

@cache
def legal_draws(cards_left, last_card):
    if len(cards_left) == 0:
        return 1 # found legal combination

    player = (n_cards - len(cards_left)) // 2
    second_card = len(cards_left) % 2 == 1

    # use list for indexing
    cards_left = list(cards_left)

    n_legal_draws = 0
    for i in range(len(cards_left)):
        card = cards_left[i]
        if card == player: # cannot draw self
            continue
        if second_card and card == last_card:
            continue # cannot draw same person

        # draw card, from copy
        new_cards_left = cards_left.copy()
        new_last_card = new_cards_left.pop(i)
        n_legal_draws += legal_draws(tuple(new_cards_left), new_last_card)

    return n_legal_draws


n_legal = legal_draws(tuple(cards), -1)

print(n_legal / math.factorial(N * 2))





