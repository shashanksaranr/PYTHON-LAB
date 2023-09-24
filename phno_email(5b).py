import re
phone_regex=re.compile(r'\+\d{2}-\d{10}')
email_regex=re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')

with open("C:\\Users\\HP\\Desktop\\PROGRAMMING\\abc.txt","r")as f:
    for line in f:
        matches=phone_regex.findall(line)
        for match in matches:
            print(match)

        matches=email_regex.findall(line)
        for match in matches:
            print(match)


