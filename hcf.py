# NAME : ABHISHEK ANAND
# E-mail ID : abhishek6.1999@gmail.com
# Name of Program :find the HCF of the 2 integer without using recursion or Euclidean algorithm
# DATE : 20-JUNE-2021
# Caveats :None

n,m =map(int, input().split())

def hcf(n,m):
    minimum = min(n,m)

    if (n % minimum == 0 and m % minimum == 0):
        return minimum
 
    for i in range(minimum // 2, 1, -1):

        if (n % i == 0 and m % i == 0):
            return i
 
    return 1

print(hcf(n,m))