def bubble_sort(Array,n):
    for i in range(n):
        for j in range(n-1):
            
            if Array[j] > Array [j + 1]:
               Array[j],Array[j+1] = Array[j+1],Array[j]
    print(Array)

n = int(input('Enter the size of the Array :'))
Array = list(map(int,input('Enter the Array elements').split()))
Result = bubble_sort(Array,n)

                

                
                