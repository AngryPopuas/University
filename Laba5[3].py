from math import sqrt

one = [12, 25, 3, 48, 71] 
two = [5, 18, 40, 62, 98] 
three = [4, 21, 37, 56, 84]

Massive = one + two + three
Massive.sort()

Lowest = Massive[:3]
Biggest = Massive[-3:]
# Lowest
p = (Lowest[0] + Lowest[1] + Lowest[2]) / 2
print(sqrt(p * (p - Lowest[0]) * (p - Lowest[1]) * (p - Lowest[2])))
# Biggest
p = (Biggest[0] + Biggest[1] + Biggest[2]) / 2
print(sqrt(p * (p - Biggest[0]) * (p - Biggest[1]) * (p - Biggest[2])))
