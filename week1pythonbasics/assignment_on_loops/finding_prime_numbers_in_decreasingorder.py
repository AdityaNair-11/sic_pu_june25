m, n = input('Enter the m and n values :').split()
m = int(m)
n = int(n)

for i in range(n,m,-1):
    factors = 0
    for j in range(1,i+1):
        if i % j == 0:
            factors = factors + 1
    if factors == 2:
        print(i,end=" ")
  