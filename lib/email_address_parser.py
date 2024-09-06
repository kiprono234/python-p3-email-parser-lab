# your code goes here!
import re
class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        
        email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
        
        return sorted(email_pattern.findall(self.email_string))


