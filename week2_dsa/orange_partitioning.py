n = int(input('Enter the size of the Array'))
Array = list(map(int,input("Enter the Array elements").split()))
compare_orange = Array[-1]
for i in range(0,n):
        for j in range(0,n):
            if Array[j] < compare_orange :
                Array[i] ,Array[j] = Array[j],Array[i]
                j += 1
print(Array[::-1])