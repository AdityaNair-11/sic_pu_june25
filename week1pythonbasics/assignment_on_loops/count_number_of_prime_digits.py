input_number = input('Enter the Number :')
count = 0

for i in str(input_number):
    fact=0
    for j in range(1,int(i)+1):
        if int(i) % j == 0:
            fact = fact + 1
    if fact == 2:
        count = count + 1
print('The number of Prime Digits in a number =',count)
