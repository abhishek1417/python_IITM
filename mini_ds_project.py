# Q. calculate the percentage of using vowels and consonants
#    how many times he has used AND and IS from his data ?
data = "my name is abhishek anand and i live in delhi. He hates to eat mangoes and loves chola bhatura."

temp = []
vowels = 0
consonants = 0
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

length_of_paragraph = len(data)
temp= data.split(" ")

for words in temp:
    for letters in words:
        if(letters =='a') or (letters =='A'):
            a_count +=1
        elif(letters =='e') or (letters =='E'):
            e_count +=1
        elif(letters =='i') or (letters =='I'):
            i_count +=1
        elif(letters =='o') or (letters =='O'):
            o_count +=1
        elif(letters =='u') or (letters =='U'):
            u_count +=1
            
