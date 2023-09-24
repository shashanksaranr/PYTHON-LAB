m1=int(input("Enter the marks of first test:"))
m2=int(input("Enter the marks of second test:"))
m3=int(input("Enter the marks of third test:"))

if(m1>m2):
    if(m2>m3):
        total=m1+m2
    else:
        total=m1+m3
elif(m1>m3):
    total=m1+m2
else:
    total=m2+m3

Avg=total/2
print("The average of best two test marks is:",Avg)