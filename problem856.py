import math
import random
from functools import cache

import numpy as np


# naive approach

def simulate():
    deck = list(range(13)) * 4

    total_draws = 0
    total_games = 0

    while True:
        n_draws = 52
        random.shuffle(deck)
        # for i in range(len(deck) - 1):
        #     if deck[i] == deck[i + 1]:
        #         n_draws = i + 2
        #
        # total_draws += n_draws
        total_games += 1
        if deck[0] != deck[1] and deck[1] == deck[2]:
            total_draws += 1
        #
        if total_games % 10000 == 0:


            print(total_draws / total_games, 16/17 * 3/50)

    # 39.18


N_COLORS = 4
N_CARD_PER_COLOR = 13
N_CARDS = N_COLORS * N_CARD_PER_COLOR

@cache
def bfs(deck, last=-1):
    # print(deck)
    cardsLeft = False
    solution = np.zeros(N_CARDS + 1, dtype=np.ulonglong) # solutions for depth 1-N_CARDS, +1 for out of cards


    # break early
    if np.sum(np.array(deck)) < 47:
        solution[0] += 1 # out of cards is also a solution
        return solution

    for card in range(N_CARD_PER_COLOR):
        # draw card if there is a card left
        if deck[card] > 0:
            cardsLeft = True
            if card == last:
                solution[0] += deck[card] # TODO: do we also have to multiply the else?
            else:
                # add next solution shifted (1 card) to current solution
                solution = solution + deck[card] * np.roll(bfs(tuple([deck[i] if i != card else (deck[i] - 1) for i in range(len(deck))]), card), 1)

    if not cardsLeft:
        solution[0] += 1 # out of cards is also a solution

    return solution


solutions = bfs(tuple([N_COLORS] * N_CARD_PER_COLOR))
print(solutions)
print(np.sum(solutions), math.factorial(N_CARDS))

# print(np.roll(np.array([1, 0, 0, 0]), 1))

print(solutions[0] / 52)
print(solutions[1] / (52*51), 1/17)