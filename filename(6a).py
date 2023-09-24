filename =input("Enter the filename:")
word =input("Enter the word to search:")
N =int(input("Enter the number of lines to display:"))

try:
    with open(filename,'r')as f:
        lines=f.readlines()
        print(f"First{N} lines of the file:")

        for i in range(N):
            print(lines[i])
        count=0

        for line in lines:
            words=line.split()

            for w in words:
                if w==word:
                    count+=1

        print(f"Frequency of '{word}' in the file: {count}")

except FileNotFoundError:
    print(f"File '{filename}' not found")