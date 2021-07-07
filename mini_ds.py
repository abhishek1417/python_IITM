# mini data science project



# Q. calculate the percentage of using vowels and consonants
#    how many times he has used AND and IS from his data ?
data = "my name is abhishek anand and i live in delhi. He hates to eat mangoes and loves chola bhatura."
temp=data

# 1st part
data=data.lower()

count_v=0
count_c=0
vowels=["a","e","i","o","u"]
for i in data:
    if i in vowels:
        count_v+=1
    else:
        count_c+=1

per_vow=(count_v*100)/(count_v+count_c)
per_con=(count_c*100)/(count_v+count_c)

per_vow= round(per_vow,2)
per_con= round(per_con,2)
print("% of vowel :",per_vow ,"and % of consonant :", per_con)

#2nd part
temp =temp.split(" ")
is_count =0
and_count =0
for words in temp:
    if(words == "is"):
        is_count +=1
    if(words == "and"):
        and_count +=1
print("No. of 'is':", is_count)
print("No. of 'and':", and_count)