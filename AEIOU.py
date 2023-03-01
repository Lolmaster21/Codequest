import sys #needed for readline and others
vowels = 0
cases = int(sys.stdin.readline().rstrip())#Gets the number of line

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()#Walks through each line
    for character in line: #Walks through each letter in the line 
        if character =='a' or character=='e' or character=='i'or character=='o'or character=='u':
            vowels += 1
    print(vowels)
    vowels = 0 #Reset for next line 

