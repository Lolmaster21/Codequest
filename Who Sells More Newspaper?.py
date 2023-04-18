import sys #needed for readline and others
import math
cases = int(sys.stdin.readline().rstrip())#Gets the number of line

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()#Walks through each line
    data = line.split(" ")#creates spaces
        
    for i in range (len(data)):
        data[i] = int(data[i])

    if data[0]  > data[1]:
        
        sub = data[0] - data[1]

        print("Times has", sub, "more subscribers")
    
    elif data[1] > data[0]:
        sub = data[1] - data[0]
        
        print("Herald has", sub, "more subscribers")
    else:
        print("Times and Herald have the same number of subscribers")
    

