# NAME : ABHISHEK ANAND
# E-mail ID : abhishek6.1999@gmail.com
# Name of Program : list program
# DATE : 20-JUNE-2021
# Caveats :None

list_1 = ["Abhishek", "Anand", "Delhi", "India", 110092,  True]

print(list_1[0])    #read 1st input
print(list_1[-1])   #read last input

#count the length of list
print(len(list_1))
# or 
count=0
for i in list_1:
    count +=1
print(count)

# Create a list of numbers in an empty list
empty_list= []
for i in range(10,30):
    empty_list.append(i)
print(empty_list)

# add element in the begining of the list
list_1.insert(0,"Mr.")
print(list_1)