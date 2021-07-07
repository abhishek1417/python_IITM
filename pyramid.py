# NAME : ABHISHEK ANAND
# E-mail ID : abhishek6.1999@gmail.com
# Name of Program : print a pyramid of numbers.
# Caveats : None

rows = int(input("numberes of rows : "))
for i in range(0,rows):     # outer loop (rows)
    for j in range(0,i+1):  # inner loop (columns)
        print("*", end="")
    print()
    
# in reverse form   
for i in range(rows,0,-1):     # outer loop (rows)
    for j in range(i,0,-1):  # inner loop (columns)
        print("*", end="")
    print()