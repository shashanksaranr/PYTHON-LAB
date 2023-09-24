class palindrome:
    def __init__(self,value):
        self.value=value

    def is_palindrome(self):
        pass

class integerpalindrome(palindrome):
    def is_palindrome(self):
        return str(self.value)==str(self.value)[::-1]

class stringpalindrome(palindrome):
    def is_palindrome(self):
        return self.value.lower()==self.value[::-1].lower()

def check_palindrome(palindrome):
    if palindrome.is_palindrome():
        print(f"{palindrome.value} is palindrome")

    else:
        print(f"{palindrome.value} is not palindrome")

integer_palindrome=integerpalindrome(12321)
check_palindrome(integer_palindrome)

string_palindrome=stringpalindrome("MANANAM")
check_palindrome(string_palindrome)

