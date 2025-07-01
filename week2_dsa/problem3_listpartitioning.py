n, x, y = input('Enter the N, x, y values :').split()
n = int(n)
x = int(x)
y = int(y)
Array = []
print(f'Enter {n} array elements')
for i in range(n):
    elements = int(input())
    Array.append(elements)


Array.sort
print(Array)
for i in Array:
    count = Array[x] - Array[y] - 1
print(count)

