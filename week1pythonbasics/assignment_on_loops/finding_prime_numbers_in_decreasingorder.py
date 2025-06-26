m, n = input('Enter the m and n values :').split()
m = int(m)
n = int(n)
factors = 0
for i in range(m, n):
    for j in range(i):
        if i % j == 0:
            factors = factors + 1
        if factors > 2: