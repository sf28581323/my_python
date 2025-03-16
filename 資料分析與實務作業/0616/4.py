from collections import defaultdict
from random import randint
import matplotlib.pyplot as plt

n = 1000
results = defaultdict(int)
for _ in range(n):
    die_1 = randint(1, 6)
    die_2 = randint(1, 6)
    results[die_1 + die_2] += 1
plt.bar(results.keys(), results.values(), width=0.35, color='green')
plt.xlabel("values")
plt.ylabel("frequencies")
plt.show()
