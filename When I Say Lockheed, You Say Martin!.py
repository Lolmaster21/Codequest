import sys #needed for readline and others
import math
cases = int(sys.stdin.readline().rstrip())#Gets the number of line

for caseNum in range(cases):
    num = int(sys.stdin.readline().rstrip())#Gets the number of line

    if num % 7 == 0 and num % 3 == 0:
        print("LOCKHEEDMARTIN")
    
    elif num % 7 == 0:
        print("MARTIN")       
    
    elif num % 3 == 0:
        print("LOCKHEED")

    else:
        print(num)

