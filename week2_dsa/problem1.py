org_string = input('Enter the first word :')
rotated_word = input('Enter the second word :')
temp_str = rotated_word + rotated_word
if org_string in temp_str:
    print(1)
else:
    print(-1)




'''
org = sample
rot = plesam
temp = plesamplesam
therefore org in rot
'''