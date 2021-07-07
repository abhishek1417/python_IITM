# Inheritance in python

class abhishek:
    name = "Abhishek Anand"
    place = "New Delhi"
    
    def HCF(self,num1, num2):
        temp=1
        if(num1>num2):
            temp = num2
        else:
            temp =num1
        for i in range(1,temp+1):
            if(num1 % i==0) and (num2%i == 0): # main logic
                result =i
        return result

class Priya:
    def Hello_priya(self):
        return("GUVI class method Hello!")

class guvi(abhishek):   # guvi is child and abhishek is parent class
    def Hello(self):
        return("GUVI class method Hello!")
    
g=guvi()

print(g.name)
print(g.HCF(4,18))
print(g.Hello())