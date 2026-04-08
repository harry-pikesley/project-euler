threes = 0
fives = 0
fifteens = 0

for i in range(1, 1000):
  if i % 15 == 0:
    fifteens += i
  if i % 5 == 0:
    fives += i
  if i % 3 == 0:
    threes += i

total = threes + fives - fifteens

print(total)
