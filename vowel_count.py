# NAME : ABHISHEK ANAND
# E-mail ID : abhishek6.1999@gmail.com
# Name of Program :find out the total number of vowels in a name.
# DATE : 19-JUNE-2021
# Caveats : None

name= input()

a=0
e=0
i=0
o=0
u=0
for s in name:
    if s == 'a' or s == 'A':
        a += 1
    elif s == 'e' or s == 'E':
        e += 1
    elif s == 'i' or s == 'I':
        i += 1
    elif s == 'o' or s == 'O':
        o += 1
    elif s == 'u' or s == 'U':
        u += 1

print(" a's Count ", a)
print(" e's Count ", e)
print(" i's Count ", i)
print(" o's Count ", o)
print(" u's Count ", u)