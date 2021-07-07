# functions 

def abhi():
    print("Abhishek ANand")

abhi()

data = abhi()
print(data) # here 'none' is also printed 

def anand():
    """ THIS IS A ABHISHEK FUNCTION """   # doc string
    return "Abhishek"

print(anand.__doc__)