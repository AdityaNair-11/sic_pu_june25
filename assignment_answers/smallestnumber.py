number1, number2, number3 = input('Enter the three numbers :').split()
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)

if number1 < number2 and number1 < number3 :
    print(number1, "Is the smallest number")
elif number2 < number1 and number2 < number3:
    print(number2, 'Is the smallest number')
else:
    print(number3, 'Is the smallest number')
   