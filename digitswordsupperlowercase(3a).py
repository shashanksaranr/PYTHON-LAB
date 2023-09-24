s=input("Enter the sentence:")
w,d,u,l=0,0,0,0
l_w=s.split()
w=len(l_w)

for c in s:
    if c.isdigit():
        d=d+1

    elif c.isupper():
        u=u+1

    elif c.islower():
        l=l+1

print("Number of words:",w)
print("Number of digits:",d)
print("Number of Uppercase Letters:",u)
print("Number of Lower case Letters:",l)
