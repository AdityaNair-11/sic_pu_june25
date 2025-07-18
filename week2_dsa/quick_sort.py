def quick_sort(Array, low, high):
    if low < high:
        pivot_index = partition_array(Array, low, high)
        quick_sort(Array, low, pivot_index - 1)
        quick_sort(Array, pivot_index + 1, high)
def partition_array(Array, low, high):
    pivot = Array[high]
    j = low
    for i in range(low, high):
        if Array[i] < pivot:
            Array[i], Array[j] = Array[j], Array[i]
            j += 1
    Array[j], Array[high] = Array[high], Array[j]
    return j
    
N = int(input("Enter the size of the Array: "))
Array = list(map(int,input("Enter the Array elements: ").split()))
low = 0
high = N-1
result = quick_sort(Array, low, high)
print(Array)