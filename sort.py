# sort your list according to accending order 

list_1 = [100,45,36,1,10,32]
temp=0
for i in range(len(list_1)-1,0,-1):
    for j in range(i):
        if list_1[j] > list_1[j+1]:
            temp = list_1[j]
            list_1[j] = list_1[j+1]
            list_1[j+1]= temp
print(list_1)

# sort your list according to decending order
list_2 = [100,45,36,1,10,32]
temp=0
for i in range(len(list_2)-1,0,-1):
    for j in range(i):
        if list_2[j] < list_2[j+1]:
            temp = list_2[j+1]
            list_2[j+1] = list_2[j]
            list_2[j]= temp
print(list_2)
