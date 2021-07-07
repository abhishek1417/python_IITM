import re

class Abhi_Web_Scrapper:
    __email_regex= "(\w+@[a-zA-Z]+?\.[a-zA-Z]{2,6})"
    __mobile_regex ="^[9876]\d{9}"
    
    def __init__(self, data):
        self.data = data
        
    #email scrapping method
    def Email_Scrapper(self):
        result = ""
        result = re.findall(self.email_regex, self.data)
        return result
    
    #mobile scrapping method
    def Indian_Mpbile_Scrapper(self):
        tmp = []
        result = []
        tmp = list(self.data.split(" "))
        for i in tmp:
            if(re.findall(self.mobile_regex, i)):
                result.append(i[:10])
        return result
    
data = """the email od of Abhishek Anand is abhishek@example.com
        and that of Ashish is ashish@example.com 
        the mobile no. of abhishek is 9661264320 and that of
        ashish is 9876543210."""
        
Abhi_Web_Scrapper.Email_Scrapper(data)