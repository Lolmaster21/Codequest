import sys
import math
import string

cases = int(sys.stdin.readline().rstrip()) #reads lines and strips spaces

for caseNum in range(cases):#runs a for loop for test cases
    
    line = sys.stdin.readline().rstrip()#reads each line
    speed, birthday = (val for val in line.split(" "))
    speed = int(speed)
    if birthday == "true":
        if speed <=65:
            print("no ticket")
            
        if speed >= 65:
            print("small ticket")
        
        if speed >= 86:
            print("big ticket")
    else:
        if speed <=60:
            print("no ticket")
            
        if speed >= 60:
            print("small ticket")
        
        if speed >= 81:
            print("big ticket")

