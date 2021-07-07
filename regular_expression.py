# regular expression or RegEX

import re # import the regular expression module of python

data = """the email od of Abhishek Anand is abhishek@example.com
        and that of Ashish is ashish@example.com 
        the mobile no. of abhishek is 9661264320 and that of
        ashish is 9876543210."""
        
# find out all the email ID from this string of characters

email_regex= "(\w+@[a-zA-Z]+?\.[a-zA-Z]{2,6})"
result = re.findall(email_regex, data)
print(result)

# find out all the Mob. No. from this string of characters
mobno_regex ="[9876]\d{9}"
result1 = re.findall(mobno_regex, data)
print(result1)

    #or
mobno_regex ="^[9876]\d{9}"
tmp = list(data.split(" "))
result2 =[]
for i in tmp:
    if(re.findall(mobno_regex, i)):
        result2.append(i[:10])
print(result2)