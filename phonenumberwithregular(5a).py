import re
def phno(numStr):
    ph_no_pattern=re.compile(r'^\d{3}-\d{3}-\d{4}$')

    if ph_no_pattern.match(numStr):
        return True
    else:
        return False

ph_num=input("Enter a phone number:")

if phno(ph_num):
    print("Valid Phone Number")
else:
    print("Invalid Phone NUmber!!")