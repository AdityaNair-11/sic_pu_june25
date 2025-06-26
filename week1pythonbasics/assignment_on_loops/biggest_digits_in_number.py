input_number = int(input('Enter the Number :'))
biggest_digit = 0
for i in str(input_number):
    if int(i) > biggest_digit:
        biggest_digit = int(i)
print('Biggest digit is :',biggest_digit)

