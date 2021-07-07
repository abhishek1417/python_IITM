# write a program in pythom to add tuples to a list.

data = (10, 20, 30)

output = []
output.append(data[0])

for i in range(1,len(data)):
    sum = data[i] +data[i-1]
    output.append(sum)
print(output)