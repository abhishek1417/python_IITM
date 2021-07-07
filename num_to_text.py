#Write a Python code to read an integer in a file e.g 123 and convert it to words e.g One hundred and twenty three and write the result #back to the same file such that your file will have "123 One hundred and twenty three " in it

import inflect
num = open('sample.txt').read()
number = int(num)

p = inflect.engine()
p.number_to_words(number)

f = open("sample.txt", "a")
i = 1
while i < 2:
    f.write(str(my_list))
    i = i + 1
f.close()

f = open("sample.txt", "r")
print(f.read())