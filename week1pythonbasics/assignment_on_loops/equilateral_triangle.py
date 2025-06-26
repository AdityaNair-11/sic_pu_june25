input = int(input('Enter the number of Lines :'))
for i in range(1,input + 1):
    for j in range(1,input+1):
        if i + j >= input+1:
            print('*',end = " ")
        else:
            print(" ",end=" ")
    for k in range(i-1):
        print('*',end=" ")
    print()








'''
equilateral triangle:

n=5


'''