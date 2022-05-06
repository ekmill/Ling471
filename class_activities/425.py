
import random as rand

heads = sum(rand.choices([0, 1])[0] == 1 for f in range(1000000))
print(heads)