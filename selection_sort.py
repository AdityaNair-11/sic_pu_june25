def selection_sort(Array,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if Array[j] < Array[i]:
                Array[i] ,Array[j] = Array[j],Array[i]
    print(Array)

n = int(input('Enter the size of the Array'))
Array = list(map(int,input("Enter the Array elements").split()))
Result = selection_sort(Array,n)