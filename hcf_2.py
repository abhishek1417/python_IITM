# write a program to calculate the HCF of numbers.

def HCF(num1, num2):
    temp=1
    if(num1>num2):
        temp = num2
    else:
        temp =num1
    for i in range(1,temp+1):
        if(num1 % i==0) and (num2%i == 0): # main logic
            result =i
    return result

print("The HCF/GCD is : ",HCF(3,9))


