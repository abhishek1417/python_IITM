#scope of a variable in a function

number =34  #global variable 
print (number)

def suman():
    number=420 #local  variable
    print(number)

suman()

# to access the variable outside the function 
# we use global variable like :

def abhi():
    global number 
    number = 12
    print(number) 

abhi()
print(number)