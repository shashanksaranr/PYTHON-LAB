import re
def pn(numStr):
    if len(numStr)!=12:
        return False

    for i in range(len(numStr)):
        if i==3 or i==7:
            if numStr[i]!="-":
                return False

        else:
            if numStr[i].isdigit()==False:
                return False

        return True
ph_num=input("Enter a phone number:")

if pn(ph_num):
    print("Valid Phone NUmber")

else:
    print("Invalid Phone Number!!")