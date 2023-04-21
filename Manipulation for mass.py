import sys #needed for readline and others
import math
cases = int(sys.stdin.readline().rstrip())#Gets the number of line

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()#Walks through each line
    data = line.split(" ")#creates spaces
        
    for i in range (len(data)):
        data[i] = float(data[i])

    
    sum = data[0] * data[1]
    
    print("%.2f" % sum) #"%.2f": Rounds up to the 2 decimal 
