# 20 digits
# 3 next < 9
from collections import defaultdict

# start met dict met alle tweetallen: 1
duos = defaultdict(int)
for i in range(100):
    duos[(i // 10), i % 10] = 1

for n in range(20 - 2):
    # maak nieuwe dict
    new_duos = defaultdict(int)
    # per tweetal kijk welke getallen ervoor kunnen
    for duo in duos:
        for i in range(0 if n < 17 else 1, 10): # skip zero for last digit!
            if i + sum(duo) > 9:
                continue
            new_duos[(i, duo[0])] += duos[duo]
    duos = new_duos

print(sum(duos.values()))



