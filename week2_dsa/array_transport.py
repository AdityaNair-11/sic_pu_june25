n = int(input('Enter the size of the original list :'))
print("Enter the values of the original list")
org_list = []
for i in range(n):
    values = int(input())
    org_list.append(values)
m = int(input('Enter the size of the missing list :'))
print("Enter the values of the missing list")
mis_list = []
for i in range(m):
    values = int(input())
    mis_list.append(values)
org_list.sort()
mis_list.sort()
output = []
for i in org_list:
    for j in mis_list:
        if i == j:
            mis_list.remove(j)
result = mis_list
print(set(result)) 

