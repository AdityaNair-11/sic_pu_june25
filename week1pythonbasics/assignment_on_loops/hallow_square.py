input = int(input('Enter the number of lines'))
for i in range(1,input+1):
    for j in range(1,input+1):
        if i == 1 or i == input or j == 1 or j == input:
            print('*', end = " ")
        else:
            print(" ",end = " ")
        

    print()
    