import sys
import math
import string

cases = int(sys.stdin.readline().rstrip()) #reads lines and strips spaces

for caseNum in range(cases):#runs a for loop for test cases
    line = sys.stdin.readline().rstrip()#reads each line
    
    newList = line.split(" ")#puts the line into a list, split up by spaces
    
    for j in range(len(newList)):#convert each lost in the list from a string into a number
        
        newList[j] = int(newList[j])
        
    newList.sort()#This sorts the list 
    
    print(newList[(len(newList))-1])#the biggest number will be the last slot sorted
