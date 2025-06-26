input_number = int(input('Enter the Nth term :'))
first_term = 1
second_term = 2
for i in range(3,input_number + 1):
    Nth_term = first_term + second_term
    first_term = second_term
    second_term = Nth_term
print('The Nth Fibo Term is :',Nth_term)





'''''
1 2 3 5 8

logic= nth term +previous term
'''''