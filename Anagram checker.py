import sys
import string
cases = int(sys.stdin.readline().rstrip()) #rstrip takes off spaces and holds a number

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip() #This holds words
    print(line, "=", end = " ") #Prints first part 
    
    #split the line into 2 variables(splits in the |)
    first, second = (value for value in line.split(" | "))
    first.rstrip() #get rid of any spaces
    second.rstrip()
    first = sorted(first) #Puts stuff in order
    second = sorted(second)
    if first == second:
        print("ANAGRAM")
    else:
        print("NOT A ANAGRAM")
