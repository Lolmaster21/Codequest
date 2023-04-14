import sys #needed for readline and others
cases = int(sys.stdin.readline().rstrip())#Gets the number of line
thing = []

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()#Walks through each line
    
    
    thing.append(line)
    
    thing.sort()
    
for i in range(cases):
    print(thing[i])

