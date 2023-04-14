import sys #needed for readline and others
cases = int(sys.stdin.readline().rstrip())#Gets the number of line
thing = []


for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()#Walks through each line
    
    length = len(line) # Lists the length of the string 
    
    length= line[length::-1] # Pushes everything to the right 
    
    print(length) # print the reversed string
     
     
