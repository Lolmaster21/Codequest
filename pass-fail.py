import sys #needed for readline and others
cases = int(sys.stdin.readline().rstrip())#Gets the number of line


for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()#Walks through each line
    data = line.split(" ")#creates spaces
    
    for i in range (len(data)):
        data[i] = int(data[i])
    
    if data[0]  <= 69:
        print("FAIL")
        
    else:
        print("PASS")
