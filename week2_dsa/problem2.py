N = int(input('Enter the Number of Requests :'))
server1 = []
for i in range (N):
    req = int(input('Enter the memory allocation or deallocation :'))
    if i % 2 == 0:
        server1.append(req)

print('The total number of memory allocation/deallocation by server 1 is :',sum(server1))



