str1=input("Enter the String 1:\n")
str2=input("Enter the String 2:\n")

if len(str2)<len(str1):
    short=len(str2)
    long=len(str1)
else:
    short=len(str1)
    long=len(str2)

matchCnt=0

for i in range(short):
    if str1[i]==str2[i]:
        matchCnt+=1
print("String similarity between two stings:")
print(matchCnt/long)