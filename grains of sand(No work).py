import sys #needed for readline and others
cases = int(sys.stdin.readline().rstrip())#Gets the number of line


for caseNum in range(cases):
    num = int(sys.stdin.readline().rstrip())#Walks through each line
    line = sys.stdin.readline().rstrip()#Walks through each line
    data = line.split(" ")#creates space
    
    for j in range (len(data)):
        data[j] = int(data[j])
        
    for i in range (num):
        sand = int(sys.stdin.readline().rstrip())#Walks through each line   
        data.append(sand)                      
    
    sum = data[0] + data[1] + data[2]
    
    print(sum)

