def binary_search(Array,key,low,high):
    while high > low:
        mid = high + low / 2
        if mid == key:
            print('The element is found at the index',Array[mid])
        elif mid > key:
            high = mid - 1
        else:
            low = mid + 1

Array = list(map(int,input('enter the array elements').split()))
key = int(input('Enter the element to be searched'))
Array.sort()
high = Array[-1]
low = Array[0]
binary_search(Array,key,low,high)
   

