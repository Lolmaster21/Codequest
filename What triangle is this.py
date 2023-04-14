import sys #needed for readline and others
cases = int(sys.stdin.readline().rstrip())#Gets the number of line


for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()#Walks through each line
    data = line.split(", ")#creates spaces
    
    for i in range (len(data)):
        data[i] = int(data[i])
    
    if data[0] + data[1] <= data[2] or data[1] + data[2] <= data[0] or data[2] + data[0] <= data[1]:
        print("Not a Triangle")
        
    else:
        if data[0] == data[1] == data[2]:
            print("Equilateral")
        
        elif data[0] == data[1] != data[2] or data[1] == data[2] != data[0] or data[2] == data[0] != data[1]:
            print("Isosceles")
            
        elif data[0] != data[1] != data[2] or data[1] != data[2] != data[0] or data[2] != data[0] != data[1]:
            print("Scalene")
        
    
       
    
