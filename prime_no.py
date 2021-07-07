# check for prime number

list_1 = [23,44,56,88,100,120]

list_2 = []

for i in list_1:
    flag=0
    for j in range (2,int(i/2)+1):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        list_2.append(i)
print(list_2)

