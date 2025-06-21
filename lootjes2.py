from functools import cache
import numpy as np
from tabulate import tabulate

Ns = [3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 50, 100, 1000, 10000]
n = 1000000

def shuffle_cards(cards, split):
    if split:
        # shuffle part
        np.random.shuffle(cards[:len(cards) // 2])
        np.random.shuffle(cards[len(cards) // 2:])
    else:
        # shuffle all
        np.random.shuffle(cards)

def is_legal(cards):
    return not (np.any(cards == original) or np.any(cards[:len(cards) // 2] - cards[len(cards) // 2:] == 0))

table = [['N', 'one draw', 'two draws', 'ratio']]

for N in Ns:
    n_cards = 2 * N

    original = np.array(list(range(1, N + 1)) * 2)  # do not use 0

    n_full = 0
    n_split = 0
    for i in range(n):
        cards_full = original.copy()
        shuffle_cards(cards_full, False)
        cards_split = original.copy()
        shuffle_cards(cards_split, True)

        if is_legal(cards_full):
            n_full += 1
        if is_legal(cards_split):
            n_split += 1

    print(f"Chance not having to redraw for N={N}:")
    print(f"Normal: {n_full} / {n} = {n_full / n}")
    print(f"Split: {n_split} / {n} = {n_split / n}")
    print(f"Ratio normal/split = {n_full / n_split}")
    row = [N, n_full / n, n_split / n, n_full / n_split]
    table.append(row)


print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

# Chance not having to redraw for N=3:
# Normal: 89281 / 1000000 = 0.089281
# Split: 55457 / 1000000 = 0.055457
# Ratio normal/split = 1.6099139874136719

# Chance not having to redraw for N=5:
# Normal: 60727 / 1000000 = 0.060727
# Split: 38276 / 1000000 = 0.038276
# Ratio normal/split = 1.5865555439439858

# Chance not having to redraw for N=10:
# Normal: 72050 / 1000000 = 0.07205
# Split: 44759 / 1000000 = 0.044759
# Ratio normal/split = 1.6097321209142295

# Chance not having to redraw for N=20:
# Normal: 77168 / 1000000 = 0.077168
# Split: 47587 / 1000000 = 0.047587
# Ratio normal/split = 1.6216193498224305

# Chance not having to redraw for N=50:
# Normal: 79658 / 1000000 = 0.079658
# Split: 49325 / 1000000 = 0.049325
# Ratio normal/split = 1.6149619868220983

# Chance not having to redraw for N=100:
# Normal: 81245 / 1000000 = 0.081245
# Split: 49539 / 1000000 = 0.049539
# Ratio normal/split = 1.640020993560629












# ╒═════╤════════════╤═════════════╤═════════╕
# │   N │   one draw │   two draws │   ratio │
# ╞═════╪════════════╪═════════════╪═════════╡
# │   3 │   0.089062 │    0.055254 │ 1.61187 │
# ├─────┼────────────┼─────────────┼─────────┤
# │   4 │   0.057147 │    0.041827 │ 1.36627 │
# ├─────┼────────────┼─────────────┼─────────┤
# │   5 │   0.060961 │    0.03856  │ 1.58094 │
# ├─────┼────────────┼─────────────┼─────────┤
# │   6 │   0.065396 │    0.041074 │ 1.59215 │
# ├─────┼────────────┼─────────────┼─────────┤
# │   7 │   0.067505 │    0.042261 │ 1.59734 │
# ├─────┼────────────┼─────────────┼─────────┤
# │   8 │   0.069343 │    0.043233 │ 1.60394 │
# ├─────┼────────────┼─────────────┼─────────┤
# │   9 │   0.070403 │    0.044011 │ 1.59967 │
# ├─────┼────────────┼─────────────┼─────────┤
# │  10 │   0.07112  │    0.044571 │ 1.59566 │
# ╘═════╧════════════╧═════════════╧═════════╛